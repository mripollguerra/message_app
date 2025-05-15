from fastapi import FastAPI
from api.v1.company.company_router import router as company_router
from api.v1.message.message_router import router as message_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Message App To Clean Architecture",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json"
    )

    # Incluir routers
    app.include_router(company_router)
    app.include_router(message_router)

    return app