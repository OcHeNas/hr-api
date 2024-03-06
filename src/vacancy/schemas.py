from datetime import datetime

from pydantic import BaseModel

class vacancyCreate(BaseModel):
    id_vacancy: int
    department_id: int
    Post: str
    Description: str
    appilicant_id: str

class appilicantCreate(BaseModel):
    id_appilicant: int
    FIO: str
    Passport: str
    INN: str
    Birthday: str
    Gender: str
    Address:str
    Resume: str
    email:str