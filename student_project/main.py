from student import Student
from student_manager import StudentManager


# ==========================================
# DISPLAY MENU
# ==========================================
def display_menu():
    print("\n" + "=" * 45)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add/Update Marks")
    print("7. View Student Report")
    print("8. Show Top Student")
    print("9. Show Class Statistics")
    print("10. Sort Students")
    print("11. Filter Students by Grade")
    print("12. Exit")

    print("=" * 45)


# ==========================================
# REGISTER STUDENT
# ==========================================
def register_student(manager):
    print("\n--- REGISTER STUDENT ---")

    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    # Validate age
    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    gender = input("Enter gender: ").strip()
    course = input("Enter course: ").strip()

    # Validate year
    while True:
        try:
            year = int(input("Enter year of study: "))

            if year <= 0:
                print("Year must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    student = Student(
        student_id,
        name,
        age,
        gender,
        course,
        year
    )

    try:
        manager.add_student(student)
        manager.save_students()

        print("\nStudent registered successfully!")

    except ValueError as error:
        print(f"\nError: {error}")


# ==========================================
# VIEW ALL STUDENTS
# ==========================================
def view_all_students(manager):
    print("\n--- ALL STUDENTS ---")

    students = manager.get_all_students()

    if not students:
        print("No students registered.")
        return

    for student in students:
        print(
            f"ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Course: {student.course} | "
            f"Year: {student.year} | "
            f"Average: {student.calculate_average():.2f} | "
            f"Grade: {student.get_grade()}"
        )


# ==========================================
# SEARCH STUDENT
# ==========================================
def search_student(manager):
    print("\n--- SEARCH STUDENT ---")

    keyword = input("Enter student ID or name: ").strip()

    results = manager.search_students(keyword)

    if not results:
        print("No students found.")
        return

    print("\nSearch Results:")

    for student in results:
        print(
            f"ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Course: {student.course} | "
            f"Average: {student.calculate_average():.2f}"
        )


# ==========================================
# UPDATE STUDENT
# ==========================================
def update_student(manager):
    print("\n--- UPDATE STUDENT ---")

    student_id = input("Enter student ID: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print("Press Enter if you want to keep the current value.")

    name = input(f"Name [{student.name}]: ").strip()
    gender = input(f"Gender [{student.gender}]: ").strip()
    course = input(f"Course [{student.course}]: ").strip()

    # Age
    age_input = input(f"Age [{student.age}]: ").strip()

    if age_input:
        try:
            age = int(age_input)

            if age <= 0:
                print("Age must be greater than 0.")
                return

        except ValueError:
            print("Invalid age.")
            return
    else:
        age = None

    # Year
    year_input = input(f"Year [{student.year}]: ").strip()

    if year_input:
        try:
            year = int(year_input)

            if year <= 0:
                print("Year must be greater than 0.")
                return

        except ValueError:
            print("Invalid year.")
            return
    else:
        year = None

    try:
        manager.update_student(
            student_id,
            name=name or None,
            age=age,
            gender=gender or None,
            course=course or None,
            year=year
        )

        manager.save_students()

        print("Student updated successfully.")

    except ValueError as error:
        print(f"Error: {error}")


# ==========================================
# DELETE STUDENT
# ==========================================
def delete_student(manager):
    print("\n--- DELETE STUDENT ---")

    student_id = input("Enter student ID: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print(f"Student: {student.name}")

    confirmation = input(
        "Are you sure you want to delete this student? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        try:
            manager.delete_student(student_id)
            manager.save_students()

            print("Student deleted successfully.")

        except ValueError as error:
            print(f"Error: {error}")

    else:
        print("Deletion cancelled.")


# ==========================================
# ADD / UPDATE MARKS
# ==========================================
def add_mark(manager):
    print("\n--- ADD / UPDATE MARK ---")

    student_id = input("Enter student ID: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    subject = input("Enter subject: ").strip()

    while True:
        try:
            mark = float(input("Enter mark (0-100): "))

            if mark < 0 or mark > 100:
                print("Mark must be between 0 and 100.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    try:
        manager.add_mark(student_id, subject, mark)
        manager.save_students()

        print("Mark saved successfully.")

    except ValueError as error:
        print(f"Error: {error}")


# ==========================================
# VIEW STUDENT REPORT
# ==========================================
def view_report(manager):
    print("\n--- STUDENT REPORT ---")

    student_id = input("Enter student ID: ").strip()

    student = manager.get_student(student_id)

    if student is None:
        print("Student not found.")
        return

    print()
    print(student.generate_report())


# ==========================================
# SHOW TOP STUDENT
# ==========================================
def show_top_student(manager):
    print("\n--- TOP STUDENT ---")

    student = manager.get_top_student()

    if student is None:
        print("No students with marks available.")
        return

    print(f"Student ID : {student.student_id}")
    print(f"Name       : {student.name}")
    print(f"Average    : {student.calculate_average():.2f}")
    print(f"Grade      : {student.get_grade()}")


# ==========================================
# CLASS STATISTICS
# ==========================================
def show_class_statistics(manager):
    print("\n--- CLASS STATISTICS ---")

    total_students = manager.count_students()
    class_average = manager.calculate_class_average()

    print(f"Total Students : {total_students}")
    print(f"Class Average  : {class_average:.2f}")

    top_student = manager.get_top_student()
    lowest_student = manager.get_lowest_student()

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


# ==========================================
# SORT STUDENTS
# ==========================================
def sort_students(manager):
    print("\n--- SORT STUDENTS ---")

    print("1. Sort by Name")
    print("2. Sort by Average")

    choice = input("Choose an option: ").strip()

    if choice == "1":

        students = manager.sort_by_name()

        print("\nStudents sorted by name:")

        for student in students:
            print(
                f"{student.student_id} - "
                f"{student.name} - "
                f"{student.calculate_average():.2f}"
            )

    elif choice == "2":

        students = manager.sort_by_average()

        print("\nStudents sorted by average:")

        for student in students:
            print(
                f"{student.student_id} - "
                f"{student.name} - "
                f"{student.calculate_average():.2f}"
            )

    else:
        print("Invalid choice.")


# ==========================================
# FILTER BY GRADE
# ==========================================
def filter_students(manager):
    print("\n--- FILTER STUDENTS BY GRADE ---")

    grade = input("Enter grade (A, B, C, D, F): ").strip().upper()

    if grade not in ["A", "B", "C", "D", "F"]:
        print("Invalid grade.")
        return

    students = manager.filter_by_grade(grade)

    if not students:
        print(f"No students found with grade {grade}.")
        return

    print(f"\nStudents with grade {grade}:")

    for student in students:
        print(
            f"{student.student_id} - "
            f"{student.name} - "
            f"{student.calculate_average():.2f}"
        )


# ==========================================
# MAIN PROGRAM
# ==========================================
def main():

    # Create StudentManager object
    manager = StudentManager()

    # Load existing students from JSON
    manager.load_students()

    print("\nWelcome to the Student Management System!")

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

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

        elif choice == "12":
            manager.save_students()

            print("\nStudent data saved.")
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1-12.")


# ==========================================
# START PROGRAM
# ==========================================
if __name__ == "__main__":
    main()
