from a2wsgi import ASGIMiddleware

from app.main import app as asgi_app

# Render fallback command: gunicorn your_application.wsgi
# Gunicorn expects a WSGI callable named `application` by default.
application = ASGIMiddleware(asgi_app)
