class Student:
    """
    Represents a student in the Student Management System.
    """

    def __init__(self, student_id, name, age, gender, subject, year):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.suject = subject
        self.year = year
        self.marks = {}

    def add_mark(self, subject, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")

        self.marks[subject] = mark

    def calculate_average(self):
        if not self.marks:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()

        if average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def get_status(self):
        if self.calculate_average() >= 50:
            return "PASS"

        return "FAIL"

    def generate_report(self):
        report = []

        report.append("=" * 45)
        report.append("STUDENT REPORT CARD")
        report.append("=" * 45)

        report.append(f"Student ID : {self.student_id}")
        report.append(f"Name: {self.name}")
        report.append(f"Age: {self.age}")
        report.append(f"Gender: {self.gender}")
        report.append(f"Subject: {self.subject}")
        report.append(f"Year: {self.year}")

        report.append("-" * 45)
        report.append("MARKS")
        report.append("-" * 45)

        if self.marks:
            for subject, mark in self.marks.items():
                report.append(f"{subject:<15}: {mark}")
        else:
            report.append("No marks recorded.")

        report.append("-" * 45)
        report.append(f"Average: {self.calculate_average():.2f}")
        report.append(f"Grade: {self.get_grade()}")
        report.append(f"Status: {self.get_status()}")
        report.append("=" * 45)

        return "\n".join(report)

    def to_dict(self):
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
        student = cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["gender"],
            data["subject"],
            data["year"]
        )

        student.marks = data.get("marks", {})

        return student

