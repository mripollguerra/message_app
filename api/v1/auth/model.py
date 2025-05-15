from pydantic import BaseModel, Field
    
class AuthRequest(BaseModel):
    email: str = Field(...)
    password: str = Field(...)