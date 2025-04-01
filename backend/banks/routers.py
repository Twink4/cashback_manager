from fastapi import APIRouter

router = APIRouter(
    prefix="/banks",
    tags=["Банки"]
)

@router.get("")
async def get_banks():
    return "Bank list"