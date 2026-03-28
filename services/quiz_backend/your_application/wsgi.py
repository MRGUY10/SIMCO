from pathlib import Path
import sys

from a2wsgi import ASGIMiddleware

# Ensure repository root is in sys.path when Render rootDir is services/quiz_backend
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.quiz_backend.main import app as asgi_app

# Gunicorn default target: gunicorn your_application.wsgi
application = ASGIMiddleware(asgi_app)
