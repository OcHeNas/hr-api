from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.vacancy.models import vacancy
from src.vacancy.models import appilicant
from src.vacancy.schemas import vacancyCreate
from src.vacancy.schemas import appilicantCreate

router1 = APIRouter(
    prefix="/vacancy",
    tags=["vacancy"]
)

@router1.get("/")
async def get_specific_vacancy(Description: str, session: AsyncSession = Depends(get_async_session)):
    query = select(vacancy).where(vacancy.c.Description == Description)
    result = await session.execute(query)
    return result.all()

@router1.post("/")
async def add_specific_vacancy(new_vacancy: vacancyCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.delete("/")
async def delete_specific_vacancy(Description: str, session: AsyncSession = Depends(get_async_session)):
    query = delete(vacancy).where(vacancy.c.Description == Description)
    result = await session.execute(query)
    return result.all()

router2 = APIRouter(
    prefix="/appilicant",
    tags=["appilicant"]
)

@router2.get("/")
async def get_specific_appilicant(email: str, session: AsyncSession = Depends(get_async_session)):
    query = select(appilicant).where(appilicant.c.email == email)
    result = await session.execute(query)
    return result.all()

@router2.post("/")
async def add_specific_appilicant(new_appilicant: appilicantCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(appilicant).values(**new_appilicant.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.delete("/")
async def delete_specific_appilicant(email: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(appilicant).where(appilicant.c.email == email)
    result = await session.execute(query)
    return result.all()