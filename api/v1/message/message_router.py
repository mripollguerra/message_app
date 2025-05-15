from fastapi import APIRouter, Depends, status, Header
from api.security.jwt_service import JWTService
from containers import Container
from dependency_injector.wiring import inject, Provide
from utils.response import ResponseHandler
from api.security.auth_dependency import authenticate_user
from application.message_application import MessageApplication

router = APIRouter(prefix="/message", tags=["Message"])

@router.post("/send/")
@inject
def send_message(
        x_services_name: str = Header(default=None),
        message_application: MessageApplication = Depends(Provide[Container.message_application]),
        # current_user = Depends(authenticate_user)
    ):
    
    results = message_application.send_messages(x_services_name)
    return results