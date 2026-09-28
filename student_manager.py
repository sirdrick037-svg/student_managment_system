import json
import os

from student import Student


class StudentManager:
    """
    Manages all student records.
    """

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}

    def add_student(self, student):
        """Add a new student to the system."""

        if student.student_id in self.students:
            raise ValueError("A student with this ID already exists.")

        self.students[student.student_id] = student

    def get_student(self, student_id):
        """Find a student using their ID."""

        return self.students.get(student_id)

    def get_all_students(self):
        """Return all students."""

        return list(self.students.values())

    def update_student(self, student_id, name=None, age=None,
                       gender=None, subject=None, year=None):
        """Update student information."""

        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        if name:
            student.name = name

        if age is not None:
            student.age = age

        if gender:
            student.gender = gender

        if subject:
            student.subject = subject

        if year is not None:
            student.year = year

    def delete_student(self, student_id):
        """Delete a student from the system."""

        if student_id not in self.students:
            raise ValueError("Student not found.")

        del self.students[student_id]

    def search_students(self, keyword):
        """Search students by ID or name."""

        keyword = keyword.lower()

        results = []

        for student in self.students.values():

            if (
                keyword in student.student_id.lower()
                or keyword in student.name.lower()
            ):
                results.append(student)

        return results

    def add_mark(self, student_id, subject, mark):
        """Add or update a student's mark."""

        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.add_mark(subject, mark)

    def get_top_student(self):
        """Return the student with the highest average."""

        students_with_marks = [
            student
            for student in self.students.values()
            if student.marks
        ]

        if not students_with_marks:
            return None

        return max(
            students_with_marks,
            key=lambda student: student.calculate_average()
        )

    def get_lowest_student(self):
        """Return the student with the lowest average."""

        students_with_marks = [
            student
            for student in self.students.values()
            if student.marks
        ]

        if not students_with_marks:
            return None

        return min(
            students_with_marks,
            key=lambda student: student.calculate_average()
        )

    def calculate_class_average(self):
        """Calculate the average of all student averages."""

        students_with_marks = [
            student
            for student in self.students.values()
            if student.marks
        ]

        if not students_with_marks:
            return 0

        total = sum(
            student.calculate_average()
            for student in students_with_marks
        )

        return total / len(students_with_marks)

    def filter_by_grade(self, grade):
        """Return students who have a specific grade."""

        grade = grade.upper()

        return [
            student
            for student in self.students.values()
            if student.get_grade() == grade
        ]
    
    def sort_by_name(self):
        """Return students sorted alphabetically."""

        return sorted(
            self.students.values(),
            key=lambda student: student.name.lower()
        )

    def sort_by_average(self, descending=True):
        """Return students sorted by average."""

        return sorted(
            self.students.values(),
            key=lambda student: student.calculate_average(),
            reverse=descending
        )
    
    def save_students(self):
        """Save all students to JSON."""

        data = {
            student_id: student.to_dict()
            for student_id, student in self.students.items()
        }

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        """Load students from JSON."""

        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.students = {
                student_id: Student.from_dict(student_data)
                for student_id, student_data in data.items()
            }

        except json.JSONDecodeError:
            print("Warning: Could not read the student data file.")
            self.students = {}

    def count_students(self):
        """Return the number of students."""

        return len(self.students)

