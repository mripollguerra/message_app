from pydantic_settings import BaseSettings

class ServiceConfig(BaseSettings):
    TWILIO_API_KEY: str
    TWILIO_SECRET_KEY: str
    EMAIL_ADDRESS: str
    EMAIL_PASSWORD: str
    WHATSAPP_API_URL: str
    WHATSAPP_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Instancia global de configuración
settings = ServiceConfig()