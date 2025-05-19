from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class MessageTemplate:
    uuid: str
    message_service: str
    name: str
    template: str
    
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    is_active: Optional[bool] = True

