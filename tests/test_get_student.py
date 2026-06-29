from pathlib import Path

from fastapi.testclient import TestClient

from app.api.student_routes import student_service
from app.main import app


client = TestClient(app)
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def test_get_student_by_id_returns_student(monkeypatch):
    monkeypatch.setattr(student_service, "data_file", FIXTURES_DIR / "students.json")

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul.sharma@example.com",
        "phone": "9876543210",
        "department": "Computer Science",
        "year": 3,
    }


def test_get_student_by_id_returns_404_when_missing(monkeypatch):
    monkeypatch.setattr(student_service, "data_file", FIXTURES_DIR / "empty_students.json")

    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}
