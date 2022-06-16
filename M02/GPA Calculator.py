# Name: Austin Kelley
# File Name: GPA Calculator
# This app will allow the user to enter a students
# name and gpa and will return whether or not the
# student made the deans list or honor roll

# Asks for students last name
last_name = input("Please enter students last name: ")
if last_name == 'ZZZ' or last_name == 'zzz':
    exit()
# Asks for students first name
first_name = input("Please enter students first name: ")


# Asks for students grade
grade = float(input("Please enter students grade: "))

# If statements
if grade >= 3.5:
    print('last_name, first_name' "is on the Dean's List.")
elif grade < 3.5:
    print('last_name, first_name' "is on the Honor Roll.")
