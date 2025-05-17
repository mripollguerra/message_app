from pydantic_settings import BaseSettings

class ServiceConfig(BaseSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_ACCOUNT_TOKEN: str
    TWILIO_PHONE_NUMBER: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instancia global de configuración
settings = ServiceConfig()