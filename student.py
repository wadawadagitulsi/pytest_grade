
import sys

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def display_result(name, marks):
    grade = calculate_grade(marks)
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Student"
    marks = int(sys.argv[2]) if len(sys.argv) > 2 else 75

    if name == "":
        name = "Student"

    if marks == "":
        marks = 75

    display_result(name, marks)
   