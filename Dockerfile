# This Dockerfile is for deploying the FastAPI backend on Render or similar platforms.
# It is a copy of backend/Dockerfile for compatibility with platforms expecting a root Dockerfile.

FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY backend .

# Install Ollama
RUN apt-get update && apt-get install -y curl zstd && \
	curl -fsSL https://ollama.com/install.sh | sh

EXPOSE 8000
EXPOSE 11434

CMD bash -c 'ollama serve & sleep 3 && ollama pull mistral && uvicorn main:app --host 0.0.0.0 --port 8000'
