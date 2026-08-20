import sqlite3


def create_connection():
    conn = sqlite3.connect("student_enrolment.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Student table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL
        )
    """)

    # Lecturer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lecturers (
            lecturer_id INTEGER PRIMARY KEY,
            lecturer_name TEXT NOT NULL
        )
    """)

    # Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_code TEXT NOT NULL UNIQUE,
            course_name TEXT NOT NULL,
            lecturer_id INTEGER,
            FOREIGN KEY (lecturer_id) REFERENCES lecturers(lecturer_id)
        )
    """)

    # Enrolment table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrolments (
            enrolment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            enrolment_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database tables created successfully.")

create_tables()
