from domain.message.service import IMessageService
from config.settings import settings

class EmailService(IMessageService):
    def __init__(self):
        self.email = settings.EMAIL_ADDRESS
        self.password = settings.EMAIL_PASSWORD

    def SendMessage(self) -> bool:
        print("Sending email")
        return True