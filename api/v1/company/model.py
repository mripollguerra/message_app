from pydantic import BaseModel, Field
from typing import  List
from api.v1.message.model import ProviderRequest
    
class CompanyCreateRequest(BaseModel):
    role_id: int = Field(...)
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    password: str = Field(...)
    
class CompanyAddProviderRequest(BaseModel):
    providers: List[ProviderRequest] = Field(...)