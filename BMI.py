
def main():
    # User information
    weight = 70  # weight in kilograms

    # Height: 5'2" converted to meters
    height = 1.5748  # height in meters

    # Calculate BMI
    bmi = weight / (height * height)

    # Display result
    print("BMI Calculator")
    print("Weight:", weight, "kg")
    print("Height: 5'2\"")
    print("Your BMI is:", round(bmi, 2))

    # Determine BMI category
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")


# Run the program
if __name__ == "__main__":
    main()