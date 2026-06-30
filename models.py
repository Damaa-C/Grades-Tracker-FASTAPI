# this is database table,describes db table structure and columns
# we write a python class and sqlalchemy turns it into a table in the database

# Columns are defined as class attributes, and their types are specified using SQLAlchemy's column types (e.g., Integer, String, Float)
# Integer: Represents an integer column in the database.
# String: Represents a string (text) column in the database.    
# Float: Represents a floating-point column in the database.
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Student(Base):
    __tablename__ = "students"  # specifies the name of the table in the database that this class represents

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable=False)
    course = Column(String,nullable=False)
    grade = Column(Float,default=0.0)  # default value for grade is set to 0.0
    email = Column(String, unique=True)
