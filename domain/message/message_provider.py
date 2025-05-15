from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class MessageProvider:
    name: str
    service_name: str

    @classmethod
    def get_providers(cls) -> List["MessageProvider"]:
        return [
            cls(name="Twilio", service_name="twilio"),
            cls(name="MailJet", service_name="mailjet"),
            cls(name="WhatsApp", service_name="whatsapp"),
        ]
