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

    # ==========================================
    # ADD STUDENT
    # ==========================================
    def add_student(self, student):
        """Add a new student to the system."""

        if student.student_id in self.students:
            raise ValueError("A student with this ID already exists.")

        self.students[student.student_id] = student

    # ==========================================
    # GET STUDENT
    # ==========================================
    def get_student(self, student_id):
        """Find a student using their ID."""

        return self.students.get(student_id)

    # ==========================================
    # GET ALL STUDENTS
    # ==========================================
    def get_all_students(self):
        """Return all students."""

        return list(self.students.values())

    # ==========================================
    # UPDATE STUDENT
    # ==========================================
    def update_student(self, student_id, name=None, age=None,
                       gender=None, course=None, year=None):
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

        if course:
            student.course = course

        if year is not None:
            student.year = year

    # ==========================================
    # DELETE STUDENT
    # ==========================================
    def delete_student(self, student_id):
        """Delete a student from the system."""

        if student_id not in self.students:
            raise ValueError("Student not found.")

        del self.students[student_id]

    # ==========================================
    # SEARCH STUDENTS
    # ==========================================
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

    # ==========================================
    # ADD MARK
    # ==========================================
    def add_mark(self, student_id, subject, mark):
        """Add or update a student's mark."""

        student = self.get_student(student_id)

        if student is None:
            raise ValueError("Student not found.")

        student.add_mark(subject, mark)

    # ==========================================
    # TOP STUDENT
    # ==========================================
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

    # ==========================================
    # LOWEST STUDENT
    # ==========================================
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

    # ==========================================
    # CLASS AVERAGE
    # ==========================================
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

    # ==========================================
    # FILTER BY GRADE
    # ==========================================
    def filter_by_grade(self, grade):
        """Return students who have a specific grade."""

        grade = grade.upper()

        return [
            student
            for student in self.students.values()
            if student.get_grade() == grade
        ]

    # ==========================================
    # SORT BY NAME
    # ==========================================
    def sort_by_name(self):
        """Return students sorted alphabetically."""

        return sorted(
            self.students.values(),
            key=lambda student: student.name.lower()
        )

    # ==========================================
    # SORT BY AVERAGE
    # ==========================================
    def sort_by_average(self, descending=True):
        """Return students sorted by average."""

        return sorted(
            self.students.values(),
            key=lambda student: student.calculate_average(),
            reverse=descending
        )

    # ==========================================
    # SAVE STUDENTS
    # ==========================================
    def save_students(self):
        """Save all students to JSON."""

        data = {
            student_id: student.to_dict()
            for student_id, student in self.students.items()
        }

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # ==========================================
    # LOAD STUDENTS
    # ==========================================
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

    # ==========================================
    # STUDENT COUNT
    # ==========================================
    def count_students(self):
        """Return the number of students."""

        return len(self.students)

