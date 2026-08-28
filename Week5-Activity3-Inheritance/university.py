# University OOP Project
# This program demonstrates classes, objects, methods, and inheritance.


# Parent Class
class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name


# Student Class
class Student(Person):
    def __init__(self, person_id, name, student_id):
        super().__init__(person_id, name)
        self.student_id = student_id


# Staff Class
class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num


# General Staff Class
class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = 0

    # Calculate the hourly pay rate
    def calculate_pay_rate(self, total_pay, hours_worked):
        if hours_worked > 0:
            self.rate_of_pay = total_pay / hours_worked
        else:
            self.rate_of_pay = 0

    # Display the pay rate
    def display_pay_rate(self):
        print(f"General Staff: {self.name}")
        print(f"Rate of Pay: ${self.rate_of_pay:.2f} per hour")


# Academic Staff Class (Lecturer)
class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = []

    # Add a publication to the list
    def add_publication(self, publication):
        self.publications.append(publication)

    # Calculate the total number of publications
    def calculate_publications(self):
        return len(self.publications)

    # Display the number of publications
    def display_publications(self):
        print(f"Lecturer: {self.name}")
        print(f"Number of Publications: {self.calculate_publications()}")


# Main function
def main():

    print("UNIVERSITY STAFF SYSTEM")
    print("------------------------")

    # Create an Academic staff object (Lecturer)
    lecturer = Academic(
        "P001",
        "John Smith",
        "S001",
        "123-456-789"
    )

    # Add publications
    lecturer.add_publication("Artificial Intelligence Research")
    lecturer.add_publication("Python Programming for Beginners")
    lecturer.add_publication("Software Engineering Principles")

    # Display lecturer information
    print("\nLECTURER INFORMATION")
    lecturer.display_publications()

    # Create a General staff object
    general_staff = General(
        "P002",
        "Mary Johnson",
        "S002",
        "987-654-321"
    )

    # Calculate pay rate
    general_staff.calculate_pay_rate(1200, 40)

    # Display general staff information
    print("\nGENERAL STAFF INFORMATION")
    general_staff.display_pay_rate()


# Run the program
if __name__ == "__main__":
    main()