from typing import Dict, Optional
from .service import IMessageService
from .services.email_service import EmailService
from .services.twilio_sms_service import TwilioSmsService
from .services.whatsapp_sms_service import WhatsAppSmsService

class MessageServiceFactory:
    def __init__(self):
        self._instances: Dict[str, IMessageService] = {
            "twilio": TwilioSmsService(),
            "email": EmailService(),
            "whatsapp": WhatsAppSmsService()
        }

    def get_service(self, service_type: str) -> Optional[IMessageService]:
        return self._instances.get(service_type)
    
# Instancia global
message_factory = MessageServiceFactory()