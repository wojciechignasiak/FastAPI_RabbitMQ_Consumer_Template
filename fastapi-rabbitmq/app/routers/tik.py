from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
router = APIRouter()

@router.get("/tik")
async def tik_handler() -> JSONResponse:
    try:
        return JSONResponse( status_code=status.HTTP_200_OK,content=jsonable_encoder({"message": "tok!"}) )
    except HTTPException as e:
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error: {e}")
