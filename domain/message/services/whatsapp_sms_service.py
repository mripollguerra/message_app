from domain.message.message_service import IMessageService
from config.settings import settings

class WhatsAppSmsService(IMessageService):
    def __init__(self):
        self.api_url = settings.WHATSAPP_API_URL
        self.token = settings.WHATSAPP_TOKEN

    def SendMessage(self) -> bool:
        print("Sending WhatsApp message")
        return True