# Dockerfile for deploying Ollama service on Render or similar platforms.
# This runs only the Ollama server with the mistral model.

FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y curl zstd && \
    curl -fsSL https://ollama.com/install.sh | sh

EXPOSE 11434

CMD bash -c 'ollama serve & sleep 5 && ollama pull mistral && tail -f /dev/null'
