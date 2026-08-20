import sqlite3


def create_connection():
    conn = sqlite3.connect("student_enrolment.db")
    return conn


def question_one():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT courses.course_name,
               COUNT(enrolments.student_id)
        FROM courses
        LEFT JOIN enrolments
        ON courses.course_id = enrolments.course_id
        GROUP BY courses.course_id, courses.course_name
    """)

    results = cursor.fetchall()

    print("\nQuestion 1: Number of students registered in each course")

    for row in results:
        print(row[0], "-", row[1], "students")

    conn.close()


def question_two():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT students.student_id,
               students.student_name,
               COUNT(enrolments.course_id)
        FROM students
        JOIN enrolments
        ON students.student_id = enrolments.student_id
        GROUP BY students.student_id, students.student_name
        HAVING COUNT(enrolments.course_id) > 1
    """)

    results = cursor.fetchall()

    print("\nQuestion 2: Students enrolled in more than one course")

    for row in results:
        print(row[0], "-", row[1], "-", row[2], "courses")

    conn.close()


def main():
    question_one()
    question_two()


if __name__ == "__main__":
    main()