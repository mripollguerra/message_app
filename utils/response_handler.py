from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

class ResponseHandler:
    @staticmethod
    def success(data=None, message="Success", code=status.HTTP_200_OK):
        return JSONResponse(
            status_code=code,
            content={
                "success": True,
                "message": message,
                "data": jsonable_encoder(data)
            }
        )

    @staticmethod
    def error(message="An error occurred", code=status.HTTP_400_BAD_REQUEST, data=None):
        return JSONResponse(
            status_code=code,
            content={
                "success": False,
                "message": message,
                "data": jsonable_encoder(data)
            }
        )
