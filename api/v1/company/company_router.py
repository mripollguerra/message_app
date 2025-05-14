from fastapi import APIRouter, Depends, status, Path
from application.company_application import CompanyApplication
from api.v1.company.model import CompanyCreateRequest, AuthRequest
from api.security.jwt_service import JWTService
from containers import Container
from dependency_injector.wiring import inject, Provide
from utils.response import ResponseHandler
from api.security.auth_dependency import authenticate_user

router = APIRouter(prefix="/companies", tags=["Company"])

@router.post("/auth/")
@inject
def auth(
        request: AuthRequest, 
        service: CompanyApplication = Depends(Provide[Container.company_service])
    ):
    
    try:
        company = service.auth_company_by_email_password(request.email, request.password)
        token = JWTService.create_access_token({"sub": company.email})
        return ResponseHandler.success(data={"access_token": token, "token_type": "bearer"}, message="Companies", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/create/")
@inject
def create_company(
        company_create: CompanyCreateRequest,
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.create_company(company_create)
        return ResponseHandler.success(data=result, message="Company created", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.post("/request-keys/")
@inject
def request_keys(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        current_user = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.request_keys(current_user.id)
        return ResponseHandler.success(data=result, message="Security keys generated", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/")
@inject
def get_companies(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.get_companies()
        return ResponseHandler.success(data=result, message="Companies", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/{id}")
@inject
def get_company_by_id(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        id: int = Path(..., description="ID de la compañía"),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.get_company_by_id(id)
        return ResponseHandler.success(data=result, message="Compañía no encontrada", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.get("/my-company/")
@inject
def get_my_company(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.get_company_by_id(_.id)
        return ResponseHandler.success(data=result, message="My Company", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)