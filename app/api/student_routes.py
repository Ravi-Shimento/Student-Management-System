from fastapi import APIRouter, HTTPException, status

from app.schemas.student_schema import Student
from app.services.student_service import StudentService


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

student_service = StudentService()

@router.get("/")
def get_students():
    return student_service.get_all_students()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    return student_service.create_student(student)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id: int):
    deleted = student_service.delete_student(id)

    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
