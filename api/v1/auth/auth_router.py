from fastapi import APIRouter, Depends, status
from application.company_application import CompanyApplication
from api.v1.auth.model import AuthRequest
from api.security.jwt_service import JWTService
from containers import Container
from dependency_injector.wiring import inject, Provide
from utils.response_handler import ResponseHandler

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/sig-in/")
@inject
def sig_in(
        request: AuthRequest, 
        service: CompanyApplication = Depends(Provide[Container.company_service])
    ):
    
    try:
        company = service.auth_company_by_email_password(request.email, request.password)
        token = JWTService.create_access_token({"sub": company.email})
        return ResponseHandler.success(data={"access_token": token, "token_type": "bearer"}, message="Inicio de sesión correcto", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)