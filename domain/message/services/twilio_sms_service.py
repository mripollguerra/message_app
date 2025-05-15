from domain.message.service import IMessageService
from config.settings import settings

class TwilioSmsService(IMessageService):
    def __init__(self):
        self.api_key = settings.TWILIO_API_KEY
        self.secret_key = settings.TWILIO_SECRET_KEY

    def SendMessage(self) -> bool:
        print("Sending SMS via Twilio")
        return True