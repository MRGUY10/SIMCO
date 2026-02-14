# This Dockerfile is for deploying the FastAPI backend on Render or similar platforms.
# It is a copy of backend/Dockerfile for compatibility with platforms expecting a root Dockerfile.

FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
