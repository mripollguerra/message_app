from typing import List, Dict, Any
from domain.message.factory import MessageServiceFactory

class MessageApplication:
    def __init__(self, message_service_factory: MessageServiceFactory):
        self.message_service_factory = message_service_factory

    def send_messages(self, service_types: str) -> List[Dict[str, Any]]:
        types_list = [t.strip().lower() for t in service_types.split(",")]
        results = []
        for service_type in types_list:
            service = self.message_service_factory.get_service(service_type)
            if service is None:
                results.append({"service_type": service_type, "error": "Service type not supported"})
            else:
                success = service.SendMessage()
                results.append({"service_type": service_type, "success": success})
        return results