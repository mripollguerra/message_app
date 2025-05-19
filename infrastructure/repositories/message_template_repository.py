from domain.message_template.message_template_repository import IMessageTemplateRepository
from models.message_template import MessageTemplate
from domain.message_template.message_template import MessageTemplate as MessageTemplateDomain
from infrastructure.db.session import SessionLocal

class MessageTemplateRepository(IMessageTemplateRepository):
    def __init__(self):
        self.session = SessionLocal()
        
    def get_templante_by_uidd(self, uidd: str) -> MessageTemplateDomain | None:
        message_template = self.session.query(MessageTemplate).filter(MessageTemplate.uuid == uidd).first()
        if message_template is None:
            return None
        
        return message_template.to_domain()