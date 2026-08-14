class TemperatureConverter:

    def __init__(self, temperature):
        self.temperature = temperature

    def convert(self):
        prefix = self.temperature[0].upper()
        value = float(self.temperature[1:])

        if prefix == "F":
            celsius = (value - 32) * 5 / 9
            return f"{self.temperature} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius"

        elif prefix == "C":
            fahrenheit = (value * 9 / 5) + 32
            return f"{self.temperature} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit"

        else:
            return "Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix."


def main():
    temperature = input("Enter temperature (e.g., F51 or C11): ")

    try:
        converter = TemperatureConverter(temperature)
        print(converter.convert())
    except ValueError:
        print("Invalid input. Please enter the temperature with the correct 'C' or 'F' prefix.")


main()