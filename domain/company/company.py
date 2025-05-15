from dataclasses import dataclass
from datetime import datetime
from domain.role.role import Role
from domain.message.message_provider import MessageProvider
from typing import Optional, List

@dataclass
class Company:
    role_id: int
    name: str
    email: str
    phone: str
    password : str
    
    id: Optional[int] = None
    api_key: Optional[str] = None
    secret_key: Optional[str] = None
    created_at: Optional[datetime] = None
    is_active: Optional[bool] = True
    role: Optional["Role"] = None
    providers: Optional[List[MessageProvider]] = None
    
    def check_password(self, password: str) -> bool:
        return self.password == password
    
    def check_secret_key(self, secret_key: str) -> bool:
        return self.secret_key == secret_key

