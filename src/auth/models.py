from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData, VARCHAR, TEXT, Date

from database import Base

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(50), nullable=False),
    Column("permissions", JSON),
)

department = Table(
    "department",
    metadata,
    Column("id_department", Integer, primary_key=True),
    Column("Name", VARCHAR(50), nullable=False),
    Column("Description", TEXT, nullable=False),
    Column("id_director", Integer, nullable=False),
)

post = Table(
    "post",
    metadata,
    Column("id_post", Integer, primary_key=True),
    Column("Members", Integer, nullable=False),
    Column("Salary", Integer, nullable=False),
    Column("Name", VARCHAR(100), nullable=False),
    Column("department_id", Integer, ForeignKey("department.id_department")),
)

order = Table(
    "order",
    metadata,
    Column("id_order", Integer, primary_key=True),
    Column("Type",VARCHAR(100), nullable=False),
    Column("Date", Date, nullable=False),
    Column("staff_id", Integer, nullable=False),
    Column("post_id", Integer, ForeignKey("post.id_post")),
)

user = Table(
    "user",
    metadata,
    Column("id_satff", Integer, primary_key=True),
    Column("FIO", VARCHAR(50), nullable=False),
    Column("username", VARCHAR(10), nullable=False),
    Column("hashed_password", VARCHAR(10), nullable=False),
    Column("Passport", TEXT, nullable=False),
    Column("INN", VARCHAR(12), nullable=False),
    Column("Birthday", Date, nullable=False),
    Column("Gender", VARCHAR(50), nullable=False),
    Column("order_id", Integer, ForeignKey("order.id_order")),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("department", Integer, ForeignKey("department.id_department")),
    Column("email", VARCHAR(50), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)

appilicant = Table(
    "appilicant",
    metadata,
    Column("id_appilicant", Integer, primary_key=True),
    Column("FIO", VARCHAR(50), nullable=False),
    Column("Passport", TEXT, nullable=False),
    Column("INN", VARCHAR(12), nullable=False),
    Column("Birthday", Date, nullable=False),
    Column("Gender", VARCHAR(50), nullable=False),
    Column("Address", VARCHAR(100), nullable=False),
    Column("Resume", TEXT, nullable=False),
    Column("email", VARCHAR(50), nullable=False),
)

vacancy = Table(
    "vacancy",
    metadata,
    Column("id_vacancy", Integer, primary_key=True),
    Column("department_id", Integer, nullable=False),
    Column("Post", VARCHAR(50), nullable=False),
    Column("Description", TEXT, nullable=False),
    Column("appilicant_id", Integer, ForeignKey("appilicant.id_appilicant")),
)

class User(SQLAlchemyBaseUserTable[int], Base):
    id_staff = Column(Integer, primary_key=True)
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
    hashed_password: Column(VARCHAR(10), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)