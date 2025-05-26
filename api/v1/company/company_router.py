from fastapi import APIRouter, Depends, status, Path
from application.company_application import CompanyApplication
from api.v1.company.model import CompanyCreateRequest, CompanyAddProviderRequest, CompanyUpdateRequest
from containers import Container
from dependency_injector.wiring import inject, Provide
from utils.response_handler import ResponseHandler
from api.security.auth_dependency import authenticate_user

router = APIRouter(prefix="/companies", tags=["Company"])

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
        return ResponseHandler.success(data=result, message="Compañía encontrada", code=status.HTTP_201_CREATED)
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
        return ResponseHandler.success(data=result, message="Compañia creada", code=status.HTTP_201_CREATED)
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
        return ResponseHandler.success(data=result, message="Mi compañia", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
@router.post("/request-keys/")
@inject
def request_keys(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        company = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.request_keys(company.id)
        return ResponseHandler.success(data=result, message="Llaves de seguridad generadas", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.post("/add-provider/")
@inject
def add_provider(
        providers: CompanyAddProviderRequest,
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        company = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.add_provider_by_company_id(providers, company.id)
        return ResponseHandler.success(data=result, message="Servicios de envio agregado", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.post("/active/{id}")
@inject
def active_company(
        id: int = Path(..., description="ID de la compañía"),
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.active_company(id)
        return ResponseHandler.success(data=result, message="Activo actualizado", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.put("/update/{id}")
@inject
def update_company(
        company_update: CompanyUpdateRequest,
        id: int = Path(..., description="ID de la compañía"),
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        _ = Depends(authenticate_user)
    ):
    
    try:
        result = company_service.update_company(id, company_update)
        return ResponseHandler.success(data=result, message="Compañia actualizada", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.put("/update-request-keys/")
@inject
def update_request_keys(
        company_service: CompanyApplication = Depends(Provide[Container.company_service]),
        company = Depends(authenticate_user)
    ):
    try:
        result = company_service.update_request_keys(company.id)
        return ResponseHandler.success(data=result, message="Llaves de seguridad actualizadas", code=status.HTTP_201_CREATED)
    except ValueError as e:
        return ResponseHandler.error(message=str(e), code=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return ResponseHandler.error(message="Internal server error", code=status.HTTP_500_INTERNAL_SERVER_ERROR)