from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import User
from  src.auth.base_config import current_user, fastapi_users

from src.database import get_async_session
from src.vacancy.models import vacancy
from src.vacancy.models import appilicant
from src.vacancy.schemas import vacancyCreate
from src.vacancy.schemas import appilicantCreate
from src.auth.base_config import check_user_role

router1 = APIRouter(
    prefix="/vacancy",
    tags=["vacancy"]
)

@router1.get("/", dependencies=[Depends(check_user_role(["Admin", "Employer", "User"]))])
async def get_specific_vacancy(Description: str = '', session: AsyncSession = Depends(get_async_session)):
    query = select(vacancy).where((Description) in vacancy.c.Description)
    result = await session.execute(query)
    return result.all()

@router1.post("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def add_specific_vacancy(new_vacancy: vacancyCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.delete("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def delete_specific_vacancy(Description: str, session: AsyncSession = Depends(get_async_session)):
    query = delete(vacancy).where(vacancy.c.Description == Description)
    result = await session.execute(query)
    return result.all()

@router1.put("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def update_specific_vacancy(Description: str, new_vacacy: vacancyCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(vacancy).where(vacancy.c.Description == Description)
    existing_vacancy = (await session.execute(query)).scalar_one_or_none()
    if existing_vacancy:
        stmt = (
            update(vacancy)
            .where(vacancy.c.Description == Description)
            .values(**new_vacacy.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"vacancy with description '{Description}' updated successfully"}
    else:
        return {"status": "error", "message": f"vacancy with description '{Description}' not found"}

router2 = APIRouter(
    prefix="/appilicant",
    tags=["appilicant"]
)

@router2.get("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def get_specific_appilicant(email: str = '', session: AsyncSession = Depends(get_async_session)):
    query = select(appilicant).where((email) in appilicant.c.email)
    result = await session.execute(query)
    return result.all()

@router2.post("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def add_specific_appilicant(new_appilicant: appilicantCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(appilicant).values(**new_appilicant.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.delete("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def delete_specific_appilicant(email: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(appilicant).where(appilicant.c.email == email)
    result = await session.execute(query)
    return result.all()

@router2.put("/", dependencies=[Depends(check_user_role(["Admin", "Employer"]))])
async def update_specific_appilicant(email: str, new_appilicant: appilicantCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(appilicant).where(appilicant.c.email == email)
    existing_appilicant = (await session.execute(query)).scalar_one_or_none()
    if existing_appilicant:
        stmt = (
            update(appilicant)
            .where(appilicant.c.email == email)
            .values(**new_appilicant.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"appilicant with email '{email}' updated successfully"}
    else:
        return {"status": "error", "message": f"appilicant with email '{email}' not found"}