# where actual db work happens
# we write function for each operation
from sqlalchemy.orm import Session
import models,schemas

def create_student(db: Session,student:schemas.StudentCreate):
    db_student = models.Student(**student.model_dump()) # creates a new instance of the Student model using the data from the StudentCreate schema
    db.add(db_student)
    db.commit()
    db.refresh(db_student)# reloads object from db after saving
    return db_student # returns completed student objects

# reads only one record
def get_student(db:Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first() # first() returns the first result of the query, or None if no results are found

# read all records
def get_students(db: Session):
    return db.query(models.Student).all() # all() returns a list of all results of the query
# select * from students

# update data
def update_student(db: Session, student_id: int, data:schemas.StudentUpdate):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    updates = data.model_dump(exclude_unset=True)
    for field,value in updates.items():
        setattr(student,field,value)

    db.commit()
    db.refresh(student)
    return student

# delete student
def delete_student(db:Session, student_id: int):
    # find student first, we cannot delete sth we have not found
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        return None
    db.delete(student)
    db.commit()
    return student
