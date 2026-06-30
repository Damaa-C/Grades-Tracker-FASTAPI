# entry point of our api/ where it all connects together
#creates the app,db tables, and runs the api server

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import get_db, engine

models.Base.metadata.create_all(bind=engine) # creates the database tables based on the models defined in models.py

app = FastAPI(title= "Student Grade Tracker",
              description= " Tracks student grades and provides CRUD operations for managing student records.",
              version= "1.0.0")

# CREATE
@app.post("/students",response_model= schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db,student)

# READ ALL
@app.get("/students",response_model= List[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

# READ A STUDENT
@app.get("/students/{student_id}",response_model = schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db,student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    
    return student

# UPDATE STUDENT
@app.put("/student/{student_id}",response_model= schemas.StudentResponse)
def update_student(student_id: int,student: schemas.StudentUpdate ,db: Session = Depends(get_db)):
    update_student = crud.update_student(student_id,db,student)
    if not update_student:
        raise HTTPException(404, "student already exists")
    
    return update_student

# DELETE STUDENT
@app.delete("/student/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.delete_student(db,student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    return {"message":"Student deleted successfully"}
