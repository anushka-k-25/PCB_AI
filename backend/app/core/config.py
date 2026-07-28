from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Powered PCB Defect Detection API"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///pcb_ai.db"

    MODEL_PATH: str = "weights/best.pt"

    UPLOAD_FOLDER: str = "uploads"

    RESULT_FOLDER: str = "results"

    class Config:
        env_file = ".env"


settings = Settings()