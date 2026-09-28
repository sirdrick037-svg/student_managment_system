# Student Management System

A simple **Python-based Student Management System** for managing student information, marks, grades, and academic performance.

The system uses **object-oriented programming (OOP)** and stores student records in a **JSON file**, allowing data to persist between program runs.

---

## Features

The system provides the following functionality:

* Add a new student
* View a student by ID
* View all students
* Update student information
* Delete a student
* Search students by ID or name
* Add or update subject marks
* Calculate individual student averages
* Automatically calculate grades
* Determine pass/fail status
* Generate student report cards
* Find the student with the highest average
* Find the student with the lowest average
* Calculate the class average
* Filter students by grade
* Sort students alphabetically by name
* Sort students by average marks
* Save student data to a JSON file
* Load student data from a JSON file
* Count the total number of students

---

## Project Structure

A recommended project structure is:

```text
StudentManagementSystem/
│
├── student.py
├── student_manager.py
├── main.py
├── students.json
└── README.md
```

### `student.py`

Contains the `Student` class.

The `Student` class represents an individual student and manages:

* Student details
* Subject marks
* Average calculation
* Grade calculation
* Pass/fail status
* Report card generation
* Conversion to and from dictionaries

### `student_manager.py`

Contains the `StudentManager` class.

The `StudentManager` class manages multiple student records and provides operations such as:

* Adding students
* Updating students
* Deleting students
* Searching
* Sorting
* Filtering
* Performance analysis
* Saving and loading data

### `main.py`

This file can be used to create the application's user interface, such as a command-line menu, and connect the `Student` and `StudentManager` classes.

### `students.json`

This file stores student records so that information is not lost when the application closes.

---

# Student Class

The `Student` class is responsible for representing an individual student.

## Creating a Student

A student can be created using:

```python
from student import Student

student = Student(
    "S001",
    "John Doe",
    20,
    "Male",
    "Computer Science",
    2
)
```

The constructor accepts:

| Parameter    | Description                          |
| ------------ | ------------------------------------ |
| `student_id` | Unique student identification number |
| `name`       | Student's name                       |
| `age`        | Student's age                        |
| `gender`     | Student's gender                     |
| `course`     | Student's course/program             |
| `year`       | Current academic year                |

---

# Adding Marks

Marks can be added using the `add_mark()` method.

```python
student.add_mark("Mathematics", 85)
student.add_mark("Programming", 90)
student.add_mark("Database Systems", 78)
```

Marks must be between **0 and 100**.

For example:

```python
student.add_mark("Mathematics", 105)
```

will raise:

```text
ValueError: Mark must be between 0 and 100.
```

Adding a mark for an existing subject updates the previous mark.

---

# Calculating the Average

The student's average can be calculated using:

```python
average = student.calculate_average()

print(average)
```

For example, if a student has:

```text
Mathematics: 80
Programming: 90
Database: 70
```

the average is:

```text
80.0
```

If the student has no marks, the method returns:

```text
0
```

---

# Grading System

The system calculates grades based on the student's average.

|    Average | Grade |
| ---------: | :---: |
|   80 – 100 |   A   |
| 70 – 79.99 |   B   |
| 60 – 69.99 |   C   |
| 50 – 59.99 |   D   |
|   Below 50 |   F   |

Example:

```python
print(student.get_grade())
```

Output:

```text
A
```

---

# Pass/Fail Status

A student passes when their average is **50 or higher**.

```python
print(student.get_status())
```

Possible results:

```text
PASS
```

or

```text
FAIL
```

---

# Generating a Report Card

The `generate_report()` method creates a formatted report containing the student's information, marks, average, grade, and status.

```python
print(student.generate_report())
```

Example output:

```text
=============================================
           STUDENT REPORT CARD
=============================================
Student ID : S001
Name       : John Doe
Age        : 20
Gender     : Male
Course     : Computer Science
Year       : 2
---------------------------------------------
MARKS
---------------------------------------------
Mathematics    : 85
Programming    : 90
Database       : 78
---------------------------------------------
Average    : 84.33
Grade      : A
Status     : PASS
=============================================
```

---

# StudentManager Class

The `StudentManager` class manages all students in the system.

Create a manager using:

```python
from student_manager import StudentManager

manager = StudentManager()
```

By default, student records are stored in:

```text
students.json
```

A different filename can also be specified:

```python
manager = StudentManager("data.json")
```

---

# Adding a Student

```python
student = Student(
    "S001",
    "John Doe",
    20,
    "Male",
    "Computer Science",
    2
)

manager.add_student(student)
```

Student IDs must be unique.

If an existing ID is used, the system raises:

```text
ValueError: A student with this ID already exists.
```

---

# Getting a Student

A student can be retrieved using their ID:

```python
student = manager.get_student("S001")
```

If the student does not exist, the method returns:

```python
None
```

---

# Getting All Students

```python
students = manager.get_all_students()

for student in students:
    print(student.name)
```

The method returns a list containing all students.

---

# Updating Student Information

Student information can be updated using:

```python
manager.update_student(
    "S001",
    name="Jane Doe",
    age=21,
    course="Information Technology",
    year=3
)
```

The student ID itself is not changed by this method.

If the student does not exist, the system raises:

```text
ValueError: Student not found.
```

---

# Deleting a Student

A student can be removed using:

```python
manager.delete_student("S001")
```

If the student does not exist, a `ValueError` is raised.

---

# Searching for Students

Students can be searched by either their ID or name.

```python
results = manager.search_students("john")

for student in results:
    print(student.student_id, student.name)
```

The search is **case-insensitive**.

For example:

```text
john
John
JOHN
```

will all match the same student name.

---

# Adding Marks Through StudentManager

Marks can also be added directly through the manager:

```python
manager.add_mark("S001", "Mathematics", 85)
```

This automatically finds the student and adds or updates the specified mark.

---

# Finding the Top Student

The student with the highest average can be found using:

```python
top_student = manager.get_top_student()

if top_student:
    print(top_student.name)
    print(top_student.calculate_average())
```

Students without marks are ignored.

If there are no students with marks, the method returns:

```python
None
```

---

# Finding the Lowest Student

The student with the lowest average can be found using:

```python
student = manager.get_lowest_student()

if student:
    print(student.name)
    print(student.calculate_average())
```

Students without marks are ignored.

---

# Calculating the Class Average

The class average can be calculated using:

```python
average = manager.calculate_class_average()

print(f"Class Average: {average:.2f}")
```

Only students who have at least one recorded mark are included.

---

# Filtering Students by Grade

Students can be filtered based on their grade.

```python
students = manager.filter_by_grade("A")

for student in students:
    print(student.name)
```

The grade is converted to uppercase, so the following are equivalent:

```python
manager.filter_by_grade("A")
```

and:

```python
manager.filter_by_grade("a")
```

---

# Sorting Students by Name

Students can be sorted alphabetically:

```python
students = manager.sort_by_name()

for student in students:
    print(student.name)
```

The sorting is case-insensitive.

---

# Sorting Students by Average

Students can also be sorted according to their academic average.

By default, sorting is descending:

```python
students = manager.sort_by_average()

for student in students:
    print(student.name, student.calculate_average())
```

To sort from lowest to highest:

```python
students = manager.sort_by_average(descending=False)
```

---

# Saving Student Data

Student records can be saved to a JSON file using:

```python
manager.save_students()
```

The data is stored in the configured JSON file.

A typical JSON structure looks like:

```json
{
    "S001": {
        "student_id": "S001",
        "name": "John Doe",
        "age": 20,
        "gender": "Male",
        "course": "Computer Science",
        "year": 2,
        "marks": {
            "Mathematics": 85,
            "Programming": 90,
            "Database": 78
        }
    }
}
```

---

# Loading Student Data

Previously saved data can be loaded using:

```python
manager.load_students()
```

If the JSON file does not exist, the method simp
