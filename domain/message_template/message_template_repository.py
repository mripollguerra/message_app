from abc import ABC, abstractmethod
from domain.message_template.message_template import MessageTemplate

class IMessageTemplateRepository(ABC):
    @abstractmethod
    def get_templante_by_uidd(self, uidd: str) -> MessageTemplate | None:
       pass