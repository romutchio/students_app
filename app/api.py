from .models import Student
from . import database
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/students')
def get_students(id: Optional[int] = None):
    if id:
        return database.get_by_id(id)
    return database.get_all()


@app.post('/students', response_model=Student)
def post(student: Student):
    database.insert(student)
    return student


@app.delete('/students/{student_id}')
def delete_student_by_id(student_id: int):
    database.delete(student_id)

