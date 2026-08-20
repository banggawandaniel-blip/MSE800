# ER Diagram Description

## Scenario

This ER diagram represents a Student Enrollment Management System for a university or school. A student can enrol in their chosen program or course. Before the enrolment process, the university needs the student's details, such as their full name, NID, and birthdate. When a student enrols in a course, the system records information such as the student code, course name, class code, and date of enrolment. After the enrolment process, the student can be connected to lectures and receive information such as the subject, subject code, lecture name, time, and date.

The system also connects lecturers with the subjects and lectures they teach. Each subject contains a subject code, unit, and description, while each lecturer has personal and contact details. This enables the institution to keep track of which lecturers are responsible for teaching particular subjects and lectures, as well as which students are enrolled in the lectures.
## Additional Attributes

- **Student:** Email – to store the student's email address.
- **Lecturer:** Phone_number – to store the lecturer's contact number.

## Types of Relationships

### Student and Enrollment
This is an **enrolment relationship**. A student can have multiple enrolments, while each enrolment is associated with a student.

### Lecturer and Lecture
This is a **teaching relationship**. A lecturer can teach one or more lectures.

### Lecture and Subject
This relationship connects lectures with the subjects being taught. A subject can be associated with lectures, and the lecture contains information about the subject being taught.