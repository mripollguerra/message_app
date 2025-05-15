from abc import ABC, abstractmethod
from typing import Optional

class IMessageService(ABC):
    @abstractmethod
    def SendMessage(self) -> bool:
        pass

_service_registry = {}

def register_service(service_type: str, service_class):
    _service_registry[service_type] = service_class

def get_service_class(service_type: str) -> Optional[type]:
    return _service_registry.get(service_type)