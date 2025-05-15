from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

def setup_exception_handlers(app):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = [
            {"field": ".".join(str(loc) for loc in err["loc"][1:]), "message": err["msg"]}
            for err in exc.errors()
        ]
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(errors),
        )