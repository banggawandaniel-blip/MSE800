grades = [88, 92, 78, 65, 50, 94]
for index, grade in enumerate(grades):
    # The 5th grade has index 4
    if index == 4:
        grades[index] = grade + 10
    else:
        grades[index] = grade + 5
print(grades)