from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData, VARCHAR, TEXT, Date, insert

from database import Base
from department.models import department, order, post

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(50), nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("FIO", VARCHAR(50), nullable=False),
    Column("username", VARCHAR(10), nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("Passport", TEXT, nullable=False),
    Column("INN", VARCHAR(12), nullable=False),
    Column("Birthday", Date, nullable=False),
    Column("Gender", VARCHAR(50), nullable=False),
    Column("order_id", Integer, ForeignKey(order.c.id_order)),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("role_name", VARCHAR(50), nullable=False),
    Column("department", Integer, ForeignKey(department.c.id_department)),
    Column("email", VARCHAR(50), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(50), nullable=False)
    FIO = Column(VARCHAR(50), nullable=False)
    Passport = Column(TEXT, nullable=False)
    INN = Column(VARCHAR(12), nullable=False)
    Birthday = Column(Date, nullable=False)
    Gender = Column(VARCHAR(50), nullable=False)
    order_id = Column(Integer, ForeignKey(order.c.id_order))
    department = Column(Integer, ForeignKey(department.c.id_department))
    username = Column(VARCHAR(10), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    role_name = Column(VARCHAR(50), nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
