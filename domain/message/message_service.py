from abc import ABC, abstractmethod
from pydantic import BaseModel

class IMessageService(ABC):
    @abstractmethod
    def get_param_model(self) -> type[BaseModel]:
        """Devuelve el modelo de parámetros esperado por el servicio"""
        pass
    
    @abstractmethod
    def send_message(self, request: BaseModel) -> bool:
        """Envía el mensaje con los parámetros específicos"""
        pass