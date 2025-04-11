from fastapi import APIRouter

from .schemas import SMccCodeSet

from backend.core.database import DependsSession


router = APIRouter(
    prefix="/mccs",
    tags=["Mcc Codes"]
)

@router.get("")
async def mcc_codes_get():
    return "OK"

@router.post("")
async def mcc_code_set(body: SMccCodeSet):
    return body
