# talks to api user

# pydantic is the validation library
#BaseModel is the parent class for all our schemas...same idea as Base in sqlalchemy
from pydantic import BaseModel 
# optional lets us mark some fields as not required...needed for update schema
from typing import Optional

# fields to be sent to the api user when they create a new student
class StudentCreate(BaseModel):
    name: str
    course: str
    grade: float = 0.0  # default value for grade is set to 0.0
    email: str

# what the user sends to update 
# is the schema for when someone wants to change student details
# optional because when updating a user should be able to send one field and change only that
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None
    grade: Optional[float] = None
    email: Optional[str] = None

# what api sends back to the user when they request student
#  id is included because when we send data back to the user we
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    grade: float
    email: str

    class Config: # special inner class
        from_attributes = True  # allows pydantic to read data from sqlalchemy models
        