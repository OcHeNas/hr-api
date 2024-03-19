from datetime import datetime

from pydantic import BaseModel

class departmentCreate(BaseModel):
    Name: str
    Description: str
    id_director: int

class postCreate(BaseModel):
    Members: int
    Salary: int
    Name: str
    department_id: int

class orderCreate(BaseModel):
    Type: str
    Date: datetime
    staff_id: int
    post_id: int
