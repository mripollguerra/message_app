from domain.message.message_service import IMessageService
from config.settings import settings

class MailjetService(IMessageService):
    def __init__(self):
        self.email = settings.MAILJET_ADDRESS
        self.password = settings.MAILJET_PASSWORD

    def SendMessage(self) -> bool:
        print("Sending email")
        return True