from pydantic import BaseModel
from typing import Optional

class SmsParameters(BaseModel):
    template_uuid: Optional[str] = None
    sms_to_number: str
    sms_body: str