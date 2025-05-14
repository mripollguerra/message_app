from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from domain.company.company import Company as CompanyDomain
from domain.role.role import Role as RoleDomain
from sqlalchemy.orm import relationship
from infrastructure.db.base import Base
from .role import Role
import datetime

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    api_key = Column(String, unique=True, nullable=True)
    secret_key = Column(String, nullable=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    
    role = relationship("Role", back_populates="companies")
    
    def to_domain_company(self) -> CompanyDomain:
        return CompanyDomain(
            id=self.id,
            role_id=self.role_id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            api_key=self.api_key,
            secret_key=self.secret_key,
            password=self.password,
            is_active=self.is_active,
            created_at=self.created_at,
            role=RoleDomain(
                id=self.role.id,
                name=self.role.name,
                created_at=self.role.created_at
            ) if self.role else None
        )