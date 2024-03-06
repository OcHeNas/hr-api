from sqlalchemy import Table, Column, Integer, TEXT, VARCHAR, MetaData, ForeignKey, Date

metadata = MetaData()

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
    Column("appilicant_id", Integer, ForeignKey(appilicant.c.id_appilicant)),
)
