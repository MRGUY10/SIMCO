# Gunicorn configuration for Render default startup command:
# gunicorn your_application.wsgi

worker_class = "uvicorn.workers.UvicornWorker"
workers = 1
timeout = 120
