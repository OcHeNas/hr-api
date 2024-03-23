from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import user
from database import get_async_session
from department.models import department
from department.models import order
from department.models import post
from department.schemas import departmentCreate
from department.schemas import orderCreate
from department.schemas import postCreate
from auth.base_config import check_user_role

router = APIRouter(
    prefix="/allusers",
    tags=["All Users"]
)

@router.get("/")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    return result.mappings().all()

router1 = APIRouter(
    prefix="/department",
    tags=["department"]
)
@router1.get("/"
             #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def get_specific_department(id_department: int = None, session: AsyncSession = Depends(get_async_session)):
    if id_department:
        query = select(department).where(department.c.id_department == id_department)
    else:
        query = select(department)
    result = await session.execute(query)
    return result.mappings().all()
@router1.post("/")
async def add_specific_department(new_department: departmentCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(department).values(**new_department.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.delete("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
                )
async def delete_specific_department(id_department: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(department).where(department.c.id_department == id_department)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.put("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def update_specific_department(id_department: int, new_department: departmentCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(department).where(department.c.id_department == id_department)
    existing_department = (await session.execute(query)).scalar_one_or_none()
    if existing_department:
        stmt = (
            update(department)
            .where(department.c.id_department == id_department)
            .values(**new_department.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"Department with description '{id_department}' updated successfully"}
    else:
        return {"status": "error", "message": f"Department with description '{id_department}' not found"}


router2 = APIRouter(
    prefix="/post",
    tags=["post"]
)

@router2.get("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def get_specific_post(id_post: int = None, session: AsyncSession = Depends(get_async_session)):
    if id_post:
        query = select(post).where(post.c.id_post == id_post)
    else:
        query = select(post)
    result = await session.execute(query)
    return result.mappings().all()

@router2.post("/")
async def add_specific_post(new_post: postCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(post).values(**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.delete("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
                )
async def delete_specific_post(id_post: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(post).where(post.c.id_post == id_post)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.put("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def update_specific_post(id_post: int, new_post: postCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(post).where(post.c.id_post == id_post)
    existing_post = (await session.execute(query)).scalar_one_or_none()
    if existing_post:
        stmt = (
            update(post)
            .where(post.c.id_post == id_post)
            .values(**new_post.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"post with id '{id_post}' updated successfully"}
    else:
        return {"status": "error", "message": f"post with description '{id_post}' not found"}

router3 = APIRouter(
    prefix="/order",
    tags=["order"]
)

@router3.get("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def get_specific_order(id_order: int = None, session: AsyncSession = Depends(get_async_session)):
    if id_order:
        query = select(order).where(order.c.id_order == id_order)
    else:
        query = select(order)
    result = await session.execute(query)
    return result.mappings().all()

@router3.post("/"
              #, dependencies=[Depends(check_user_role(["Admin"]))]
              )
async def add_specific_order(new_order: orderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router3.delete("/"
                #, dependencies=[Depends(check_user_role(["Admin"]))]
                )
async def delete_specific_order(id_order: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(order).where(order.c.id_order == id_order)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router3.put("/"
    #, dependencies=[Depends(check_user_role(["Admin"]))]
             )
async def update_specific_order(id_order: int, new_order: orderCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.id_order == id_order)
    existing_order = (await session.execute(query)).scalar_one_or_none()
    if existing_order:
        stmt = (
            update(order)
            .where(order.c.id_order == id_order)
            .values(**new_order.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"order with id '{id_order}' updated successfully"}
    else:
        return {"status": "error", "message": f"order with description '{id_order}' not found"}