from pydantic import BaseModel, Field
    
class ProviderRequest(BaseModel):
    name: str = Field(...)
    service_name: str = Field(...)