from student import Student
from student_manager import StudentManager

def display_menu():
    print("\n" + "=" * 60)
    print("STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add/Update Subject Mark")
    print("7. View Student Results")
    print("8. Show Top Student")
    print("9. Show Class Statistics")
    print("10. Sort Students")
    print("11. Filter Students by Grade")
    print("12. Exit")

    print("=" * 60)

def register_student(manager):

    print("\n" + "=" * 60)
    print("REGISTER STUDENT")
    print("=" * 60)

    student_id = input(
        "Enter student ID: "
    ).strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    name = input(
        "Enter student name: "
    ).strip()

    if not name:
        print("Student name cannot be empty.")
        return

    while True:

        try:

            age = int(
                input("Enter age: ")
            )

            if age <= 0:
                print(
                    "Age must be greater than 0."
                )
                continue

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    gender = input(
        "Enter gender: "
    ).strip()

    while True:

        try:

            year = int(
                input("Enter year of study: ")
            )

            if year <= 0:
                print(
                    "Year must be greater than 0."
                )
                continue

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    student = Student(
        student_id,
        name,
        age,
        gender,
        year
    )

    try:

        manager.add_student(student)

    except ValueError as error:

        print(
            f"\nError: {error}"
        )

        return

    print("\n" + "-" * 60)
    print("ENTER SCHOOL SUBJECTS")
    print("-" * 60)

    while True:

        subject = input(
            "\nEnter subject: "
        ).strip()

        if not subject:
            print(
                "Subject cannot be empty."
            )
            continue

        while True:

            try:

                mark = float(
                    input(
                        f"Enter mark for {subject}: "
                    )
                )

                if mark < 0 or mark > 100:

                    print(
                        "Mark must be between 0 and 100."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        try:

            student.add_mark(
                subject,
                mark
            )

        except ValueError as error:

            print(
                f"Error: {error}"
            )

            continue

        while True:

            another = input(
                "Add another subject? (yes/no): "
            ).strip().lower()

            if another in ["yes", "no"]:
                break

            print(
                "Please enter yes or no."
            )

        if another == "no":
            break

    manager.save_students()

    print("\n")
    print(student.generate_report())

    print(
        "\nStudent registered successfully!"
    )



def view_all_students(manager):

    print("\n--- ALL STUDENTS ---")

    students = manager.get_all_students()

    if not students:

        print(
            "No students registered."
        )

        return

    for student in students:

        print(
            f"ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Average: "
            f"{student.calculate_average():.2f} | "
            f"Grade: {student.get_grade()}"
        )

def search_student(manager):

    print("\n--- SEARCH STUDENT ---")

    keyword = input(
        "Enter student ID or name: "
    ).strip()

    results = manager.search_students(
        keyword
    )

    if not results:

        print(
            "No students found."
        )

        return

    print("\nSearch Results:")

    for student in results:

        print(
            f"ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Average: "
            f"{student.calculate_average():.2f} | "
            f"Grade: {student.get_grade()}"
        )

def update_student(manager):

    print("\n--- UPDATE STUDENT ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = manager.get_student(
        student_id
    )

    if student is None:

        print(
            "Student not found."
        )

        return

    print(
        "Press Enter to keep the current value."
    )

    name = input(
        f"Name [{student.name}]: "
    ).strip()

    gender = input(
        f"Gender [{student.gender}]: "
    ).strip()

    age_input = input(
        f"Age [{student.age}]: "
    ).strip()

    if age_input:

        try:

            age = int(age_input)

            if age <= 0:

                print(
                    "Age must be greater than 0."
                )

                return

        except ValueError:

            print(
                "Invalid age."
            )

            return

    else:

        age = None

    year_input = input(
        f"Year [{student.year}]: "
    ).strip()

    if year_input:

        try:

            year = int(year_input)

            if year <= 0:

                print(
                    "Year must be greater than 0."
                )

                return

        except ValueError:

            print(
                "Invalid year."
            )

            return

    else:

        year = None

    try:

        manager.update_student(
            student_id,
            name=name or None,
            age=age,
            gender=gender or None,
            year=year
        )

        manager.save_students()

        print(
            "Student updated successfully."
        )

    except ValueError as error:

        print(
            f"Error: {error}"
        )

def delete_student(manager):

    print("\n--- DELETE STUDENT ---")

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = manager.get_student(
        student_id
    )

    if student is None:

        print(
            "Student not found."
        )

        return

    print(
        f"Student: {student.name}"
    )

    confirmation = input(
        "Are you sure you want to delete "
        "this student? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        try:

            manager.delete_student(
                student_id
            )

            manager.save_students()

            print(
                "Student deleted successfully."
            )

        except ValueError as error:

            print(
                f"Error: {error}"
            )

    else:

        print(
            "Deletion cancelled."
        )

def add_mark(manager):

    print(
        "\n--- ADD / UPDATE SUBJECT MARK ---"
    )

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = manager.get_student(
        student_id
    )

    if student is None:

        print(
            "Student not found."
        )

        return

    subject = input(
        "Enter subject: "
    ).strip()

    if not subject:

        print(
            "Subject cannot be empty."
        )

        return

    while True:

        try:

            mark = float(
                input(
                    "Enter mark (0-100): "
                )
            )

            if mark < 0 or mark > 100:

                print(
                    "Mark must be between 0 and 100."
                )

                continue

            break

        except ValueError:

            print(
                "Please enter a valid number."
            )

    try:

        manager.add_mark(
            student_id,
            subject,
            mark
        )

        manager.save_students()

        print(
            f"{subject} mark saved successfully."
        )

    except ValueError as error:

        print(
            f"Error: {error}"
        )

def view_report(manager):

    print(
        "\n--- STUDENT RESULTS ---"
    )

    student_id = input(
        "Enter student ID: "
    ).strip()

    student = manager.get_student(
        student_id
    )

    if student is None:

        print(
            "Student not found."
        )

        return

    print()

    print(
        student.generate_report()
    )

def show_top_student(manager):

    print(
        "\n--- TOP STUDENT ---"
    )

    student = manager.get_top_student()

    if student is None:

        print(
            "No students with marks available."
        )

        return

    print(
        f"Student ID : {student.student_id}"
    )

    print(
        f"Name: {student.name}"
    )

    print(
        f"Average: "
        f"{student.calculate_average():.2f}"
    )

    print(
        f"Grade: {student.get_grade()}"
    )

def show_class_statistics(manager):

    print(
        "\n--- CLASS STATISTICS ---"
    )

    total_students = (
        manager.count_students()
    )

    class_average = (
        manager.calculate_class_average()
    )

    print(
        f"Total Students : {total_students}"
    )

    print(
        f"Class Average  : "
        f"{class_average:.2f}"
    )

    top_student = (
        manager.get_top_student()
    )

    lowest_student = (
        manager.get_lowest_student()
    )

    if top_student:

        print(
            f"Top Student    : "
            f"{top_student.name} "
            f"({top_student.calculate_average():.2f})"
        )

    if lowest_student:

        print(
            f"Lowest Student : "
            f"{lowest_student.name} "
            f"({lowest_student.calculate_average():.2f})"
        )

def sort_students(manager):

    print(
        "\n--- SORT STUDENTS ---"
    )

    print("1. Sort by Name")
    print("2. Sort by Average")

    choice = input(
        "Choose an option: "
    ).strip()

    # ------------------------------
    # SORT BY NAME
    # ------------------------------
    if choice == "1":

        students = (
            manager.sort_by_name()
        )

        print(
            "\nStudents sorted by name:"
        )

        for student in students:

            print(
                f"{student.student_id} - "
                f"{student.name} - "
                f"{student.calculate_average():.2f}"
            )

    elif choice == "2":

        students = (
            manager.sort_by_average()
        )

        print(
            "\nStudents sorted by average:"
        )

        for student in students:

            print(
                f"{student.student_id} - "
                f"{student.name} - "
                f"{student.calculate_average():.2f}"
            )

    else:

        print(
            "Invalid choice."
        )

def filter_students(manager):

    print(
        "\n--- FILTER STUDENTS BY GRADE ---"
    )

    grade = input(
        "Enter grade (A, B, C, D, F): "
    ).strip().upper()

    if grade not in [
        "A",
        "B",
        "C",
        "D",
        "F"
    ]:

        print(
            "Invalid grade."
        )

        return

    students = (
        manager.filter_by_grade(grade)
    )

    if not students:

        print(
            f"No students found with "
            f"grade {grade}."
        )

        return

    print(
        f"\nStudents with grade {grade}:"
    )

    for student in students:

        print(
            f"{student.student_id} - "
            f"{student.name} - "
            f"{student.calculate_average():.2f}"
        )

def main():

    manager = StudentManager()

    # Load saved students
    manager.load_students()

    print(
        "\nWelcome to the "
        "Student Management System!"
    )

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            register_student(manager)

        elif choice == "2":

            view_all_students(manager)

        elif choice == "3":

            search_student(manager)

        elif choice == "4":

            update_student(manager)

        elif choice == "5":

            delete_student(manager)

        elif choice == "6":

            add_mark(manager)

        elif choice == "7":

            view_report(manager)

        elif choice == "8":

            show_top_student(manager)

        elif choice == "9":

            show_class_statistics(manager)

        elif choice == "10":

            sort_students(manager)

        elif choice == "11":

            filter_students(manager)

        # ------------------------------
        # EXIT
        # ------------------------------
        elif choice == "12":

            manager.save_students()

            print(
                "\nStudent data saved."
            )

            print(
                "Thank you for using "
                "the system!"
            )

            break

        else:

            print(
                "Invalid choice. "
                "Please select 1-12."
            )

if __name__ == "__main__":
    main()

