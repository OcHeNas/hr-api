from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate, UserUpdate

from vacancy.router import router1 as router_vacancy
from vacancy.router import router2 as router_appilicant
from department.router import router1 as router_department
from department.router import router2 as post_router
from department.router import router3 as order_router

app = FastAPI(
    title="Human Resources Department"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(router_vacancy)
app.include_router(router_appilicant)
app.include_router(router_department)
app.include_router(post_router)
app.include_router(order_router)