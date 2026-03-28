"""
Configuration settings for the SIMCO backend application.
"""
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List


ENV_FILE_PATH = Path(__file__).resolve().parents[1] / ".env"
ENV_FILE_LOCAL_PATH = Path(__file__).resolve().parents[1] / ".env.local"

class Settings(BaseSettings):
    # Application
    APP_NAME: str = "SIMCO - Cognitive Evaluation System"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # API
    API_V1_PREFIX: str = "/api/v1"

    # Database
    DATABASE_URL: str = ""
    SQLITE_DB_PATH: str = "data/sessions.db"
    JSON_SESSIONS_DIR: str = "data/sessions_json"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return []
            # Accept common comma-separated env format.
            if not stripped.startswith("["):
                return [item.strip() for item in stripped.split(",") if item.strip()]
        return value
    
    # LLM provider switch: "ollama" or "mistral_api"
    LLM_PROVIDER: str = "ollama"

    # Ollama LLM
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "mistral"
    OLLAMA_TIMEOUT: int = 120

    # Hosted Mistral API
    MISTRAL_API_BASE_URL: str = "https://api.mistral.ai/v1"
    MISTRAL_API_KEY: str = ""
    MISTRAL_MODEL: str = "mistral-small-latest"
    MISTRAL_TIMEOUT: int = 60

    # SIMCO Logic (neural confidence service)
    SIMCO_LOGIC_BASE_URL: str = "https://confidence-backend-v68b.onrender.com"

    # Notification service
    NOTIFICATION_BASE_URL: str = "https://notification-simco.onrender.com"
    NOTIFICATION_TIMEOUT_SECONDS: int = 5
    
    # Session Management
    SESSION_TIMEOUT: int = 3600  # 1 hour in seconds
    
    # Quiz Settings
    DEFAULT_QUIZ_LENGTH: int = 10
    DEFAULT_TIME_LIMIT: int = 1200  # 20 minutes in seconds
    
    # Behavioral Analysis
    WEBCAM_ENABLED: bool = True
    BLINK_RATE_THRESHOLD: float = 30.0
    HEAD_MOVEMENT_THRESHOLD: float = 5.0
    GAZE_STABILITY_THRESHOLD: float = 0.6
    
    model_config = SettingsConfigDict(
        env_file=(str(ENV_FILE_PATH), str(ENV_FILE_LOCAL_PATH)),
        case_sensitive=True,
        enable_decoding=False,
    )

# Global settings instance
settings = Settings()
