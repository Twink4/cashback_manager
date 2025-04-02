from fastapi import APIRouter

from sqlalchemy import select

from ..core.database import DependsSession

router = APIRouter(
    prefix="/banks",
    tags=["Банки"]
)

@router.get("")
async def get_banks(
    session: DependsSession
):
    result = await session.execute(select(1))
    return result.scalar()