from pydantic import BaseModel, Field
    
class AuthRequest(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
    
class CompanyCreateRequest(BaseModel):
    role_id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    password: str = Field(...)