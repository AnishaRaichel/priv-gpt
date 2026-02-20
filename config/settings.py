from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_DB_URL: str
    MONGO_DB_NAME: str
    OLLAMA_URL: str
    APP_OLLAMA_MODELS: str   # ← MUST match .env exactly

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()
