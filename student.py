class Student:


 def __init__(self, student_id, name, age, gender, year):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.gender = gender
    self.year = year

    # Dictionary:
    # subject name -> mark
    self.marks = {}

def add_mark(self, subject, mark):
    """
    Add or update a mark for a subject.
    """

    if mark < 0 or mark > 100:
        raise ValueError(
            "Mark must be between 0 and 100."
        )

    self.marks[subject] = mark

def calculate_average(self):
    """
    Calculate the student's average mark.
    """

    if not self.marks:
        return 0

    total = sum(self.marks.values())

    return total / len(self.marks)

@staticmethod
def get_mark_grade(mark):
    """
    Calculate the grade for one mark.
    """

    if mark >= 80:
        return "A"

    elif mark >= 70:
        return "B"

    elif mark >= 60:
        return "C"

    elif mark >= 50:
        return "D"

    else:
        return "F"

@staticmethod
def get_grade_comment(grade):
    """
    Return a comment based on the grade.
    """

    comments = {
        "A": "Excellent work! Keep it up!",
        "B": "Very good work! Keep improving!",
        "C": "Good effort. You can do even better!",
        "D": "Fair work. More practice is needed.",
        "F": "Needs to work harder on your studies."
    }

    return comments.get(
        grade,
        "Keep working hard!"
    )

def get_grade(self):
    """
    Calculate the overall grade.
    """

    average = self.calculate_average()

    return self.get_mark_grade(average)

def get_overall_comment(self):
    """
    Get a comment for the overall grade.
    """

    grade = self.get_grade()

    return self.get_grade_comment(grade)

def get_status(self):
    """
    Determine whether the student passed or failed.
    """

    if self.calculate_average() >= 50:
        return "PASS"

    return "FAIL"

def generate_report(self):
    """
    Generate a simple student results report.
    """

    report = []

    # Heading
    report.append("=" * 40)
    report.append("             STUDENT RESULT")
    report.append("=" * 40)

    # Student information
    report.append("")
    report.append(
        f"Student ID: {self.student_id}"
    )

    report.append(
        f"Name: {self.name}"
    )

    # Subjects
    report.append("")
    report.append("Subjects:")

    if self.marks:

        for subject, mark in self.marks.items():

            report.append(
                f"{subject}: {mark:.2f}"
            )

    else:

        report.append(
            "No subjects or marks recorded."
        )

    # Results
    report.append("")
    report.append("Result:")

    report.append(
        f"Average: {self.calculate_average():.2f}"
    )

    report.append(
        f"Grade: {self.get_grade()}"
    )

    report.append(
        f"Status: {self.get_status()}"
    )

    report.append(
        f"Comment: {self.get_overall_comment()}"
    )

    # Closing line
    report.append("")
    report.append("=" * 40)

    return "\n".join(report)

def to_dict(self):
    """
    Convert the Student object into a dictionary
    so it can be saved as JSON.
    """

    return {
        "student_id": self.student_id,
        "name": self.name,
        "age": self.age,
        "gender": self.gender,
        "year": self.year,
        "marks": self.marks
    }

@classmethod
def from_dict(cls, data):
    """
    Create a Student object from dictionary data.
    """

    student = cls(
        data["student_id"],
        data["name"],
        data["age"],
        data["gender"],
        data["year"]
    )

    student.marks = data.get(
        "marks",
        {}
    )

    return student

