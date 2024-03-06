from datetime import datetime

from pydantic import BaseModel

class departmentCreate(BaseModel):
    id_department: int
    Name: str
    Description: str
    id_director: int

class postCreate(BaseModel):
    id_post: int
    Members: int
    Salary: int
    Name: str
    department_id: int

class orderCreate(BaseModel):
    id_order: int
    Type: str
    Date: str
    staff_id: int
    post_id: int
