from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def SendMessage(self) -> bool:
        pass