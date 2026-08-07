class BMI:

    def calculate(self):
        weight = 70      # kg
        height = 1.5748  # meters (5'2")

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print("BMI Calculator")
        print("Weight:", weight, "kg")
        print("Height: 5'2\"")
        print("BMI:", round(bmi, 2))
        print("Category:", category)


def main():
    bmi = BMI()
    bmi.calculate()


main()