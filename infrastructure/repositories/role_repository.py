from domain.role.role_repository import IRoleRepository
from infrastructure.models.role import Role
from infrastructure.db.session import SessionLocal
from domain.role.role import Role as RoleDomain

class RoleRepository(IRoleRepository):
    def __init__(self):
        self.session = SessionLocal()
    
    def get_role_by_id(self, role_id: int) -> RoleDomain | None:
        role = self.session.query(Role).filter(Role.id == role_id).first()
        
        # If the role is not found, return None
        return None if role is None else role.to_domain_role()
