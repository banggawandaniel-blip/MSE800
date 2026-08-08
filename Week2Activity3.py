class Student:
    def __init__(self, full_name, age, address, student_id):
        self.full_name = full_name      # String: stores the student's full name
        self.age = age                  # Integer: stores the student's age
        self.address = address          # String: stores the student's address
        self.student_id = student_id    # String: stores the Student ID


def main():
    students = []  # List: stores multiple Student objects

    number = int(input("How many students? "))  # Integer

    for i in range(number):
        print(f"\nStudent {i + 1}")

        name = input("Full name: ")       # String
        age = int(input("Age: "))         # Integer
        address = input("Address: ")      # String
        student_id = input("Student ID: ")  # String

        student = Student(name, age, address, student_id)
        students.append(student)

    # Sort students from youngest to oldest
    students.sort(key=lambda student: student.age)

    print("\n--- Students Sorted by Age ---")

    for student in students:
        print(
            f"Name: {student.full_name}, "
            f"Age: {student.age}, "
            f"Address: {student.address}, "
            f"Student ID: {student.student_id}"
        )


main()