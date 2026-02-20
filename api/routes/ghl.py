from fastapi import APIRouter, HTTPException
from services.ghl_service import GHLService

router = APIRouter(
    prefix="/ghl",
    tags=["GoHighLevel"]
)

@router.get("/usuarios")
async def get_account():
    try:
        return await GHLService.get_account_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
