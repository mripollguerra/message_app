from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from infrastructure.db.base import Base
from domain.role.role import Role as RoleDomain
import datetime

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    companies = relationship("Company", back_populates="role")
    
    def to_domain(self) -> RoleDomain:
        return RoleDomain(
                id=self.id,
                name=self.name,
                created_at=self.created_at
            )