from typing import Optional
from datetime import date

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    role_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    FIO: str
    Passport: str
    INN: str
    Birthday: date
    Gender: str
    order_id: int
    department: int
    password: str
    role_id: int
    role_name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

class UserUpdate(schemas.BaseUserUpdate):
    id: int
    username: str
    email: str
    FIO: str
    Passport: str
    INN: str
    Birthday: date
    Gender: str
    order_id: int
    department: int
    password: str
    role_id: int
    role_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False