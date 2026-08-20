from database import create_connection
import sqlite3


def add_student(student_id, student_name, date_of_birth):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (student_id, student_name, date_of_birth) VALUES (?, ?, ?)",
        (student_id, student_name, date_of_birth)
    )

    conn.commit()
    conn.close()

    print("Student added successfully.")


def add_lecturer(lecturer_id, lecturer_name):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO lecturers (lecturer_id, lecturer_name) VALUES (?, ?)",
        (lecturer_id, lecturer_name)
    )

    conn.commit()
    conn.close()

    print("Lecturer added successfully.")


def add_course(course_id, course_code, course_name, lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO courses (course_id, course_code, course_name, lecturer_id) VALUES (?, ?, ?, ?)",
        (course_id, course_code, course_name, lecturer_id)
    )

    conn.commit()
    conn.close()

    print("Course added successfully.")


def add_enrolment(student_id, course_id, enrolment_date):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO enrolments (student_id, course_id, enrolment_date) VALUES (?, ?, ?)",
        (student_id, course_id, enrolment_date)
    )

    conn.commit()
    conn.close()

    print("Enrolment added successfully.")


def view_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    return rows


def view_courses():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    conn.close()

    return rows


def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lecturers")
    rows = cursor.fetchall()

    conn.close()

    return rows


def view_enrolments():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM enrolments")
    rows = cursor.fetchall()

    conn.close()

    return rows