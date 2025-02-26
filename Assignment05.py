# ---------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and
# exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Student-PyQ,2/23/2025, Modified Script to use JSON file, load contents from
#                     json file into table list, menu option 3 writes to json
#                     file using dump method, close, and display data stored.
# ---------------------------------------------------------------------------#
# 2/23 Change: Import JSON library
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# 2/23 Change: File name changed from "Enrollments.csv" to Enrollments.json.
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered.
student_last_name: str = ''  # Holds the last name of a student entered.
course_name: str = ''  # Holds the name of a course entered.
# 2/23 Change: Added variable to hold json data.
json_data: str = ''
# 2/23 Change: Changed list to dictionary collection, set to empty.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
# 2/23 Change: Set menu_choice to empty string.
menu_choice: str = ''# Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
# 2/23 Change: Changed to read load from Json file, add try-except block.
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()


# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        # 2/23 Change: Add entered student data to dictionary collection.
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            # 2/23 Change: Modified to get value by dictionary key.
            try:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            except Exception as e:
                print("There was a error with the student data!\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # 2/23 Change: Save to json file using the dump method.
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()

        print("The following data was saved to file!")
        for student in students:
            # 2/23 Change: Modified to get value by dictionary key.
            try:
                print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            except Exception as e:
                print("There was a error with the student data!\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
