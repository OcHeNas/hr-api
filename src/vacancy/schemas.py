from datetime import datetime

from pydantic import BaseModel

class vacancyCreate(BaseModel):
    department_id: int
    Post: str
    Description: str

class appilicantCreate(BaseModel):
    FIO: str
    Passport: str
    INN: str
    Birthday:datetime
    Gender: str
    Address:str
    Resume: str
    email: str
    id_vacancy: int