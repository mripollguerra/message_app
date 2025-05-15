from domain.message.service import IMessageService
from infrastructure.db.session import SessionLocal

class MessageService(IMessageService):
    def __init__(self):
        self.session = SessionLocal()