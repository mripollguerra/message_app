from pydantic import BaseModel
from typing import Optional

class SmsParameters(BaseModel):
    template_uidd: Optional[str] = None
    sms_to_number: str
    sms_body: str