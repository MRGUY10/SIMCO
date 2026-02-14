# Dockerfile for deploying Ollama service on Render or similar platforms.
# This runs only the Ollama server with the tinyllama model (optimized for low memory).

FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y curl zstd && \
    curl -fsSL https://ollama.com/install.sh | sh

# Set Ollama to listen on all interfaces
ENV OLLAMA_HOST=0.0.0.0:11434

EXPOSE 11434

CMD bash -c 'ollama serve & sleep 5 && ollama pull tinyllama && tail -f /dev/null'
