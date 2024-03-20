from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.models import User
from  src.auth.base_config import current_user, fastapi_users

from src.database import get_async_session
from src.vacancy.models import vacancy
from src.vacancy.models import applicant
from src.vacancy.schemas import vacancyCreate
from src.vacancy.schemas import applicantCreate
from src.auth.base_config import check_user_role

router1 = APIRouter(
    prefix="/vacancy",
    tags=["vacancy"]
)

@router1.get("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer", "User"]))]
             )
async def get_specific_vacancy(id_vacancy: int = None, session: AsyncSession = Depends(get_async_session)):
    if id_vacancy:
        query = select(vacancy).where(vacancy.c.id_vacancy == id_vacancy)
    else:
        select(vacancy)
    result = await session.execute(query)
    return result.mappings().all()

@router1.post("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
              )
async def add_specific_vacancy(new_vacancy: vacancyCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(vacancy).values(**new_vacancy.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.delete("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
                )
async def delete_specific_vacancy(id_vacancy: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(vacancy).where(vacancy.c.id_vacancy == id_vacancy)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.put("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
             )
async def update_specific_vacancy(id_vacancy: int, new_vacacy: vacancyCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(vacancy).where(vacancy.c.id_vacancy == id_vacancy)
    existing_vacancy = (await session.execute(query)).scalar_one_or_none()
    if existing_vacancy:
        stmt = (
            update(vacancy)
            .where(vacancy.c.id_vacancy == id_vacancy)
            .values(**new_vacacy.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"vacancy with description '{id_vacancy}' updated successfully"}
    else:
        return {"status": "error", "message": f"vacancy with description '{id_vacancy}' not found"}

router2 = APIRouter(
    prefix="/applicant",
    tags=["applicant"]
)

@router2.get("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
             )
async def get_specific_applicant(id_applicant: int = None, session: AsyncSession = Depends(get_async_session)):
    if id_applicant:
        query = select(applicant).where(applicant.c.id_applicant == id_applicant)
    else:
        query = select(applicant)
    result = await session.execute(query)
    return result.mappings().all()

@router2.post("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer", "User"]))]
              )
async def add_specific_applicant(new_applicant: applicantCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(applicant).values(**new_applicant.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.delete("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
                )
async def delete_specific_applicant(id_applicant: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(applicant).where(applicant.c.id_applicant == id_applicant)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.put("/"
    #, dependencies=[Depends(check_user_role(["Admin", "Employer"]))]
             )
async def update_specific_applicant(id_applicant: int, new_appilicant: applicantCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(applicant).where(applicant.c.id_applicant == id_applicant)
    existing_applicant = (await session.execute(query)).scalar_one_or_none()
    if existing_applicant:
        stmt = (
            update(applicant)
            .where(applicant.c.id_applicant == id_applicant)
            .values(**new_appilicant.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"applicant with email '{id_applicant}' updated successfully"}
    else:
        return {"status": "error", "message": f"applicant with email '{id_applicant}' not found"}