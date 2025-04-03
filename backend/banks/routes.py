from fastapi import APIRouter

from sqlalchemy import select

from ..core.database import DependsSession

from .models import Banks
from .schemas import SBanksSet

router = APIRouter(
    prefix="/banks",
    tags=["Банки"]
)


@router.get("")
async def get_banks(
    session: DependsSession
):
    result = await session.execute(select(Banks.__table__.columns))
    return result.mappings().all()


@router.post("")
async def set_banks(
    session: DependsSession,
    body: SBanksSet
):
    return body
