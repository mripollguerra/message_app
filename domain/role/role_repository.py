from abc import ABC, abstractmethod
from domain.role.role import Role

class IRoleRepository(ABC):
    @abstractmethod
    def get_role_by_id(self, role_id: int) -> Role | None:
        pass
