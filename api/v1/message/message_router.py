from fastapi import APIRouter, Depends, status, Header
from api.security.jwt_service import JWTService
from containers import Container
from dependency_injector.wiring import inject, Provide
from utils.response_handler import ResponseHandler
from api.security.auth_dependency import authenticate_user
from application.message_application import MessageApplication

router = APIRouter(prefix="/message", tags=["Message"])

@router.post("/send/")
@inject
def send_message(
        x_services_name: str = Header(default=None),
        message_application: MessageApplication = Depends(Provide[Container.message_application]),
        company = Depends(authenticate_user)
    ):
    
    try:
        results = message_application.send_messages(x_services_name, company.id)
        return ResponseHandler.success(data=results, message="Providers", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/providers/")
@inject
def get_providers(
        message_application: MessageApplication = Depends(Provide[Container.message_application]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        providers = message_application.get_providers()
        return ResponseHandler.success(data=providers, message="Providers", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_500_INTERNAL_SERVER_ERROR)