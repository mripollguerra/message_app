from sqlalchemy import Column, Integer, String, Boolean, DateTime
from infrastructure.db.base import Base
from domain.message_template.message_template import MessageTemplate as MessageTemplateDomain
import datetime

class MessageTemplate(Base):
    __tablename__ = "message_templates"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, nullable=False)
    name = Column(String, nullable=False)
    message_service = Column(String, nullable=False)
    template = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    def to_domain(self) -> MessageTemplateDomain:
        return MessageTemplateDomain(
            id=self.id,
            name=self.name,
            uuid=self.uuid,
            message_service=self.message_service,
            template=self.template,
            is_active=self.is_active,
            created_at=self.created_at
        )
