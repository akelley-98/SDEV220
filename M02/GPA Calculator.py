student = input("Please enter students full name: ")
grade = float(input("Please enter students grade: "))

if grade >= 3.5:
    print(student, "is on the Dean's List.")
elif grade < 3.5:
    print(student, "is on the Honor Roll.")