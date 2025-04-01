from fastapi import Depends

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from typing import Annotated

from backend.core.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    ...

async def get_session():
    async with async_session_maker() as session:
        yield session
        
DependsSession: Annotated[AsyncSession, Depends(get_session)]