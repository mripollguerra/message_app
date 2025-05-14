from fastapi import Header, HTTPException, status, Depends
from application.company_application import CompanyApplication
from containers import Container
from dependency_injector.wiring import Provide, inject
from api.security.jwt_service import JWTService

@inject
def authenticate_user(
    x_authorization_token: str = Header(default=None),
    x_api_key: str = Header(default=None),
    x_secret_key: str = Header(default=None),
    service: CompanyApplication = Depends(Provide[Container.company_service])
):
    # Autenticación por token (por ejemplo, Bearer)
    if x_authorization_token:
        token = x_authorization_token.replace("Bearer ", "")
        payload = JWTService.verify_token(token)
        if payload is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
        
        user = service.get_company_by_email(payload.get("sub"))
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
        return user

    # Autenticación por API key
    if x_api_key and x_secret_key:
        user = service.auth_company_by_keys(x_api_key, x_secret_key)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key o Secret Key inválidos")
        return user

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autenticado")
