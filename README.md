# Student Management System

A Python-based **Student Management System** developed as a Python Module Capstone Project.

The system allows users to register students, manage student information, record marks, calculate grades, generate report cards, search students, sort and filter records, and store data permanently using JSON.

---

##  Project Overview

The Student Management System is a menu-driven console application designed to demonstrate practical Python programming concepts.

The project uses **Object-Oriented Programming (OOP)**, multiple Python modules, file handling, JSON, exception handling, functions, loops, conditionals, lists, dictionaries, list comprehensions, lambda functions, and CRUD operations.

The application is focused entirely on managing student records and academic performance.

---

##  Project Objectives

The main objectives of this project are to:

* Manage student information
* Register new students
* Search for students
* Update student information
* Delete student records
* Record and update student marks
* Calculate student averages
* Assign grades automatically
* Determine pass/fail status
* Generate student report cards
* Find the highest-performing student
* Find the lowest-performing student
* Calculate the class average
* Sort students
* Filter students by grade
* Store student data permanently
* Demonstrate different Python programming concepts

---

##  Features

### 1. Register Student

Users can register a student by providing:

* Student ID
* Name
* Age
* Gender
* Course
* Year of study

The system prevents duplicate student IDs.

---

### 2. View All Students

Displays all registered students together with:

* Student ID
* Name
* Course
* Year
* Average
* Grade

---

### 3. Search Student

Students can be searched using:

* Student ID
* Student name

The search is case-insensitive.

For example:

```text
Enter student ID or name: john
```

---

### 4. Update Student

Existing student information can be updated.

The system allows users to modify:

* Name
* Age
* Gender
* Course
* Year

Pressing Enter keeps the existing value.

---

### 5. Delete Student

Users can delete a student using their Student ID.

The system asks for confirmation before deleting the record.

---

### 6. Add or Update Marks

Marks can be recorded for different subjects.

For example:

```text
Mathematics: 85
English: 78
Science: 92
```

Marks must be between:

```text
0 - 100
```

---

### 7. Student Report Card

The system generates a report containing:

* Student details
* Subject marks
* Average
* Grade
* Pass/fail status

Example:

```text
=============================================
           STUDENT REPORT CARD
=============================================
Student ID : ST001
Name       : John Doe
Age        : 20
Gender     : Male
Course     : Computer Science
Year       : 2
---------------------------------------------
MARKS
---------------------------------------------
Mathematics    : 85
English        : 78
Science        : 92
---------------------------------------------
Average    : 85.00
Grade      : A
Status     : PASS
=============================================
```

---

## Grading System

The system calculates the grade based on the student's average.

|  Average | Grade |
| -------: | :---: |
| 80 - 100 |   A   |
|  70 - 79 |   B   |
|  60 - 69 |   C   |
|  50 - 59 |   D   |
| Below 50 |   F   |

A student passes when their average is **50 or above**.

---

##  Academic Statistics

The system can calculate:

* Top-performing student
* Lowest-performing student
* Class average
* Total number of students

This allows the application to provide basic class-level statistics.

---

## Sorting and Filtering

Students can be sorted by:

### Name

Students are displayed alphabetically.

### Average

Students are displayed according to their academic average.

### Grade Filtering

Users can filter students by:

```text
A
B
C
D
F
```

For example:

```text
Enter grade: A
```

The system will display students who currently have an A grade.

---

#  Python Concepts Demonstrated

This project demonstrates a wide range of Python programming concepts.

## Variables

Used to store student information and program data.

```python
name = "John"
age = 20
course = "Computer Science"
```

---

## Data Types

The project uses:

* Strings
* Integers
* Floats
* Lists
* Dictionaries
* Boolean values

---

## Lists

Lists are used when working with collections of students.

```python
students = manager.get_all_students()
```

---

## Dictionaries

Student marks are stored using a dictionary.

```python
student.marks = {
    "Mathematics": 85,
    "English": 78,
    "Science": 92
}
```

Student records are also stored using dictionaries when converting objects to JSON.

---

## Tuples

Tuples can be used to represent fixed groups of values where appropriate.

---

## Sets

Sets can be used when working with unique values such as unique subjects or identifiers.

---

## Conditional Statements

The project uses:

```python
if
elif
else
```

For example, grades are assigned using conditions:

```python
if average >= 80:
    return "A"
elif average >= 70:
    return "B"
```

---

## Loops

The project uses:

* `for` loops
* `while` loops

For example, the main menu continuously runs until the user chooses Exit.

---

## Functions

The application is divided into reusable functions such as:

```python
register_student()
view_all_students()
search_student()
update_student()
delete_student()
add_mark()
view_report()
```

This keeps the program organized and easier to maintain.

---

## Object-Oriented Programming

The project uses classes and objects.

The main class is:

```python
class Student:
```

A student object can be created using:

```python
student = Student(
    student_id,
    name,
    age,
    gender,
    course,
    year
)
```

The project also uses:

```python
class StudentManager:
```

to manage multiple student objects.

---

## Constructors

The `Student` class uses the constructor:

```python
def __init__(self, student_id, name, age, gender, course, year):
```

The constructor initializes the student's information.

---

## Methods

The `Student` class contains methods such as:

```python
add_mark()
calculate_average()
get_grade()
get_status()
generate_report()
to_dict()
```

---

## Exception Handling

The project uses:

```python
try
except
```

to handle invalid user input.

For example:

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid number.")
```

This prevents the application from crashing because of invalid input.

---

## List Comprehensions

List comprehensions are used to efficiently filter students.

Example:

```python
students_with_marks = [
    student
    for student in self.students.values()
    if student.marks
]
```

---

## Lambda Functions

Lambda functions are used when sorting students.

Example:

```python
sorted(
    self.students.values(),
    key=lambda student: student.name.lower()
)
```

---

## File Handling

The system stores data in a JSON file.

The project uses:

```python
open()
```

to read and write files.

---

## JSON

Student records are stored in:

```text
students.json
```

JSON makes it possible to keep student information after the program is closed.

---

# Project Structure

```text
student-management-system/
│
├── main.py
├── student.py
├── student_manager.py
├── students.json
└── README.md
```

### `main.py`

Contains the application's user interface and menu system.

Responsible for:

* User input
* Menu display
* Calling the appropriate functions
* Handling user interaction

---

### `student.py`

Contains the `Student` class.

Responsible for:

* Student information
* Marks
* Average calculation
* Grade calculation
* Pass/fail status
* Report generation

---

### `student_manager.py`

Contains the `StudentManager` class.

Responsible for:

* Adding students
* Searching students
* Updating students
* Deleting students
* Sorting students
* Filtering students
* Calculating class statistics
* Saving and loading data

---

### `students.json`

Stores student records permanently.

This file is automatically created when student data is saved.

---

### `README.md`

Contains the documentation for the project.

---

# How to Run the Project

## Step 1: Open the Project Folder

Open the project folder in your code editor or terminal.

---

## Step 2: Make Sure Python Is Installed

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 3: Run the Program

Run:

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

# Main Menu

When the program starts, you will see:

```text
=============================================
       STUDENT MANAGEMENT SYSTEM
=============================================

1. Register Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Add/Update Marks
7. View Student Report
8. Show Top Student
9. Show Class Statistics
10. Sort Students
11. Filter Students by Grade
12. Exit
=============================================
```

---

# Example Usage

### Register a student

```text
Enter your choice: 1

Enter student ID: ST001
Enter student name: John Doe
Enter age: 20
Enter gender: Male
Enter course: Computer Science
Enter year of study: 2

Student registered successfully!
```

### Add marks

```text
Enter your choice: 6

Enter student ID: ST001
Enter subject: Mathematics
Enter mark: 85

Mark saved successfully.
```

Repeat this for other subjects.

---

# Data Persistence

The system automatically saves student information to:

```text
students.json
```

For example:

```json
{
    "ST001": {
        "student_id": "ST001",
        "name": "John Doe",
        "age": 20,
        "gender": "Male",
        "course": "Computer Science",
        "year": 2,
        "marks": {
            "Mathematics": 85,
            "English": 78,
            "Science": 92
        }
    }
}
```

When the application starts again, the saved information is loaded automatically.

---

# CRUD Operations

The project demonstrates the four basic CRUD operations.

| Operation
