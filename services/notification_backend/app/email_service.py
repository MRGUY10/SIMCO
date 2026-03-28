import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from .settings import settings
from .schemas import NotificationRequest
from .pdf_service import build_result_pdf


def resolve_smtp_host(host: str, port: int) -> str:
    if not settings.MAIL_FORCE_IPV4:
        return host
    try:
        infos = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
        if infos:
            return infos[0][4][0]
    except OSError:
        pass
    return host


def build_email_subject(percentage: float) -> str:
    if percentage >= 80:
        return "SIMCO - Résultat Excellent 🎉"
    if percentage >= 60:
        return "SIMCO - Bon Résultat ✅"
    if percentage >= 40:
        return "SIMCO - Résultat Intermédiaire 📘"
    return "SIMCO - Résultat et Plan d'Action"


def build_email_body(payload: NotificationRequest) -> str:
    return (
        f"Bonjour {payload.user_name},\n\n"
        "Votre résultat SIMCO est en pièce jointe. Merci de le consulter.\n\n"
        "Équipe SIMCO"
    )


def send_notification_email(payload: NotificationRequest) -> tuple[bool, str]:
    if settings.MAIL_AUTH and (not settings.MAIL_USERNAME or not settings.MAIL_PASSWORD):
        return False, "mail_credentials_missing"

    sender = settings.MAIL_USERNAME
    recipient = payload.user_email
    subject = build_email_subject(payload.quiz_result.percentage)
    body = build_email_body(payload)

    message = MIMEMultipart()
    message["From"] = f"{settings.MAIL_FROM_NAME} <{sender}>" if sender else settings.MAIL_FROM_NAME
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain", "utf-8"))

    # PDF attachment with result statistics
    pdf_bytes = build_result_pdf(payload)
    pdf_attachment = MIMEApplication(pdf_bytes, _subtype="pdf")
    pdf_attachment.add_header("Content-Disposition", "attachment", filename="simco_result_report.pdf")
    message.attach(pdf_attachment)

    timeout_seconds = max(
        settings.MAIL_CONNECTION_TIMEOUT_MS,
        settings.MAIL_TIMEOUT_MS,
        settings.MAIL_WRITE_TIMEOUT_MS,
    ) / 1000.0
    smtp_host = resolve_smtp_host(settings.MAIL_HOST, settings.MAIL_PORT)

    try:
        with smtplib.SMTP(smtp_host, settings.MAIL_PORT, timeout=timeout_seconds) as server:
            if settings.MAIL_STARTTLS:
                server.starttls()
            if settings.MAIL_AUTH:
                server.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            server.sendmail(sender, [recipient], message.as_string())
        return True, "notification_sent"
    except OSError as exc:
        if settings.SOFT_FAIL_ON_SMTP_NETWORK_ERROR and getattr(exc, "errno", None) in {101, 113, -2, 11001}:
            return True, f"notification_deferred_network_unreachable: {exc}"
        return False, f"send_failed: {exc}"
    except Exception as exc:
        return False, f"send_failed: {exc}"
