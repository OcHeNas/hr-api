from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.department.models import department
from src.department.models import order
from src.department.models import post
from src.department.schemas import departmentCreate
from src.department.schemas import orderCreate
from src.department.schemas import postCreate

router1 = APIRouter(
    prefix="/department",
    tags=["department"]
)

@router1.get("/")
async def get_specific_department(Description: str = '', session: AsyncSession = Depends(get_async_session)):
    query = select(department).where((Description) in department.c.Description)
    result = await session.execute(query)
    return result.all()

@router1.post("/")
async def add_specific_department(new_department: departmentCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(department).values(**new_department.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router1.delete("/")
async def delete_specific_department(Description: str, session: AsyncSession = Depends(get_async_session)):
    query = delete(department).where(department.c.Description == Description)
    result = await session.execute(query)
    return result.all()

@router1.put("/")
async def update_specific_department(Description: str, new_department: departmentCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(department).where(department.c.Description == Description)
    existing_department = (await session.execute(query)).scalar_one_or_none()
    if existing_department:
        stmt = (
            update(department)
            .where(department.c.Description == Description)
            .values(**new_department.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"Department with description '{Description}' updated successfully"}
    else:
        return {"status": "error", "message": f"Department with description '{Description}' not found"}


router2 = APIRouter(
    prefix="/post",
    tags=["post"]
)

@router2.get("/")
async def get_specific_post(id_post: int = '', session: AsyncSession = Depends(get_async_session)):
    query = select(post).where((id_post) in post.c.id_post)
    result = await session.execute(query)
    return result.all()

@router2.post("/")
async def add_specific_post(new_post: postCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(post).values(**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router2.delete("/")
async def delete_specific_post(id_post: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(post).where(post.c.id_post == id_post)
    result = await session.execute(query)
    return result.all()

@router2.put("/")
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

@router3.get("/")
async def get_specific_order(staff_id: int = '', session: AsyncSession = Depends(get_async_session)):
    query = select(order).where((staff_id) in order.c.staff_id)
    result = await session.execute(query)
    return result.all()

@router3.post("/")
async def add_specific_order(new_order: orderCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(order).values(**new_order.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router3.delete("/")
async def delete_specific_order(staff_id: int, session: AsyncSession = Depends(get_async_session)):
    query = delete(order).where(order.c.staff_id == staff_id)
    result = await session.execute(query)
    return result.all()

@router3.put("/")
async def update_specific_order(staff_id: int, new_order: orderCreate, session: AsyncSession = Depends(get_async_session)):
    query = select(order).where(order.c.staff_id == staff_id)
    existing_order = (await session.execute(query)).scalar_one_or_none()
    if existing_order:
        stmt = (
            update(order)
            .where(order.c.staff_id == staff_id)
            .values(**new_order.dict())
        )
        await session.execute(stmt)
        await session.commit()
        return {"status": "success", "message": f"order with id '{staff_id}' updated successfully"}
    else:
        return {"status": "error", "message": f"order with description '{staff_id}' not found"}