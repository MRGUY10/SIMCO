from pathlib import Path
import sys

# Ensure repository root is in sys.path when Render rootDir is services/quiz_backend
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from services.quiz_backend.main import app as asgi_app

# Gunicorn default target: gunicorn your_application.wsgi
# `application` is intentionally ASGI. Gunicorn will run it correctly
# when worker_class is set to `uvicorn.workers.UvicornWorker`
# (see gunicorn.conf.py).
application = asgi_app
