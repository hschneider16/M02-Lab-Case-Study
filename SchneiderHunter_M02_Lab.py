# M02 Case Study
# By Hunter Schneider
# 1/23/2024
# This program allows the user to enter a student's name and their GPA. Using the GPA, the program will determine if the student
# is on the Dean's List, Honor Roll, or neither.

while True:
    # Get the user's input
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    # End loop if ZZZ is entered
    if last_name == 'ZZZ':
        break

    # Inputs for both GPA and first name
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    # Checking the GPA to see if it is greater than or equal to the required amount for Dean's List/Honor Roll
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")