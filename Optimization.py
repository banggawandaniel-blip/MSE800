def isfloat(value):
    try:
        return float(value)
    except ValueError:
        return False


def inputfloat(message):
    while True:
        number = isfloat(input(message))
        if number is not False:
            return number
        print("Please enter a valid number.")


class BMIcalculator:

    def getdata(self):
        self.w = inputfloat("Please enter your weight in kilograms: ")
        self.h = inputfloat("Please enter your height in centimetres: ") / 100

    def calculate(self):
        return round(self.w / (self.h ** 2), 2)


def main():
    print("=" * 42)
    print("Hello, let's calculate your BMI.\n")

    calc = BMIcalculator()
    calc.getdata()

    bmi = calc.calculate()
    print(f"Your BMI is {bmi}")

    print("=" * 42)


if __name__ == "__main__":
    main()