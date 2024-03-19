from sqlalchemy import Table, Column, Integer, TEXT, VARCHAR, MetaData, ForeignKey, Date

metadata = MetaData()

department = Table(
    "department",
    metadata,
    Column("id_department", Integer, primary_key=True, autoincrement=True),
    Column("Name", VARCHAR(50), nullable=False),
    Column("Description", TEXT, nullable=False),
    Column("id_director", Integer, nullable=False),
)

post = Table(
    "post",
    metadata,
    Column("id_post", Integer, primary_key=True, autoincrement=True),
    Column("Members", Integer, nullable=False),
    Column("Salary", Integer, nullable=False),
    Column("Name", VARCHAR(100), nullable=False),
    Column("department_id", Integer, ForeignKey(department.c.id_department)),
)

order = Table(
    "order",
    metadata,
    Column("id_order", Integer, primary_key=True, autoincrement=True),
    Column("Type",VARCHAR(100), nullable=False),
    Column("Date", Date, nullable=False),
    Column("staff_id", Integer, nullable=False),
    Column("post_id", Integer, ForeignKey(post.c.id_post)),
)