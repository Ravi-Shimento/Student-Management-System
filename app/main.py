from fastapi import FastAPI
from app.api.student_routes import router as student_router



app = FastAPI(
    title="Student Management System",
    version="1.0.0",
    description="Backend API for managing students."
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Management System"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Student Management System"
    }


app.include_router(student_router)
