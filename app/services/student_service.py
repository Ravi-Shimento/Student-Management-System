import json
from pathlib import Path


class StudentService:

    def __init__(self):
        self.data_file = Path("data/students.json")


    
    def load_students(self):
        """Load all students from the JSON file."""

        if not self.data_file.exists():
            return []

        try:
            with open(self.data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_students(self, students):
        """Save students to the JSON file."""

        with open(self.data_file, "w") as file:
            json.dump(students, file, indent=4)

    def get_next_id(self, students):
        """Generate the next student ID."""

        if not students:
            return 1

        return max(student["id"] for student in students) + 1


    def get_all_students(self):
        """Get all students data from json """

        return self.load_students()

    
    def create_student(self, student):
        """create a new student data send it to save function """
        students = self.load_students()

        student_dict = student.model_dump()

        student_dict["id"] = self.get_next_id(students)

        students.append(student_dict)

        self.save_students(students)

        return student_dict