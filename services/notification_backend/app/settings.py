from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


ENV_FILE_PATH = Path(__file__).resolve().parents[1] / ".env"
ENV_FILE_LOCAL_PATH = Path(__file__).resolve().parents[1] / ".env.local"


class Settings(BaseSettings):
    MAIL_HOST: str = "smtp.gmail.com"
    MAIL_PORT: int = 587
    MAIL_FORCE_IPV4: bool = True
    MAIL_USERNAME: str = "kamdem.guy@institutsaintjean.org"
    MAIL_PASSWORD: str = "krcmwwfwnomgwmgi"
    MAIL_STARTTLS: bool = True
    MAIL_AUTH: bool = True
    MAIL_SSL_TRUST: str = "smtp.gmail.com"
    MAIL_CONNECTION_TIMEOUT_MS: int = 5000
    MAIL_TIMEOUT_MS: int = 3000
    MAIL_WRITE_TIMEOUT_MS: int = 5000
    MAIL_FROM_NAME: str = "SIMCO Notifications"
    SOFT_FAIL_ON_SMTP_NETWORK_ERROR: bool = False
    API_PORT: int = 8020

    model_config = SettingsConfigDict(
        env_file=(str(ENV_FILE_PATH), str(ENV_FILE_LOCAL_PATH)),
        case_sensitive=True,
    )


settings = Settings()
