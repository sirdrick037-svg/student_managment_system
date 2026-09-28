class Student:
    """
    Represents a student in the Student Management System.
    """

    def __init__(self, student_id, name, age, gender, year):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.year = year

        # Dictionary for subjects and marks
        self.marks = {}

    def add_mark(self, subject, mark):
        """
        Add or update a subject mark.
        """

        if mark < 0 or mark > 100:
            raise ValueError(
                "Mark must be between 0 and 100."
            )

        self.marks[subject] = mark

    def calculate_average(self):
        """
        Calculate the student's overall average.
        """

        if not self.marks:
            return 0

        return sum(self.marks.values()) / len(self.marks)

    @staticmethod
    def get_mark_grade(mark):
        """
        Calculate the grade for a mark.
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
        Calculate the student's overall grade.
        """

        average = self.calculate_average()

        return self.get_mark_grade(average)

    def get_overall_comment(self):
        """
        Return a comment based on the overall grade.
        """

        grade = self.get_grade()

        return self.get_grade_comment(grade)

    def get_status(self):
        """
        Determine whether the student has passed.
        """

        if self.calculate_average() >= 50:
            return "PASS"

        return "FAIL"

    def generate_report(self):
        """
        Generate a complete student results report.
        """

        report = []

        report.append("=" * 80)
        report.append(
            "STUDENT RESULTS"
        )
        report.append("=" * 80)

        report.append(
            f"Student ID: {self.student_id}"
        )

        report.append(
            f"Name: {self.name}"
        )

        report.append(
            f"Age: {self.age}"
        )

        report.append(
            f"Gender: {self.gender}"
        )

        report.append(
            f"Year       : {self.year}"
        )

        report.append("-" * 80)

        report.append(
            f"{'SUBJECT':<20}"
            f"{'MARK':<10}"
            f"{'GRADE':<10}"
            f"COMMENT"
        )

        report.append("-" * 80)

        if self.marks:

            for subject, mark in self.marks.items():

                grade = self.get_mark_grade(mark)

                comment = self.get_grade_comment(
                    grade
                )

                report.append(
                    f"{subject:<20}"
                    f"{mark:<10.2f}"
                    f"{grade:<10}"
                    f"{comment}"
                )

        else:

            report.append(
                "No subjects or marks recorded."
            )

        report.append("-" * 80)

        overall_grade = self.get_grade()

        overall_comment = self.get_overall_comment()

        report.append(
            f"Average       : "
            f"{self.calculate_average():.2f}"
        )

        report.append(
            f"Overall Grade : "
            f"{overall_grade}"
        )

        report.append(
            f"Status        : "
            f"{self.get_status()}"
        )

        report.append(
            f"Comment       : "
            f"{overall_comment}"
        )

        report.append("=" * 80)

        return "\n".join(report)

    def to_dict(self):
        """
        Convert Student object into a dictionary
        for JSON storage.
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
        Create a Student object from JSON data.
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

