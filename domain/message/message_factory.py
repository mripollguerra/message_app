from typing import Dict, Optional
from .message_service import IMessageService
from .services.twilio_sms_service import TwilioSmsService

class MessageFactory:
    def __init__(self):
        self._instances: Dict[str, IMessageService] = {
            "twilio": TwilioSmsService(),
        }

    def get_service(self, service_type: str) -> Optional[IMessageService]:
        return self._instances.get(service_type)
    
message_factory = MessageFactory()