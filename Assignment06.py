# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Student-PyQ,3/4/25,Update to include classes (FileProcessor, IO) to include
#                      descriptive document strings. Add functions to include (descriptive
#                      document strings, except blocks, staticmethod decorator)
#                      - output_error_messages(message: str, error: Exception = None)
#                      - output_menu(menu: str)
#                      - input_menu_choice()
#                      - output_student_course(student_data: list)
#                      - input_student_data(student_data: list)
#                      - read_data_from_file(file_name: str, student_data: list)
#                      - write_data_to_file(file_name: str, student_data: list)
# ------------------------------------------------------------------------------------------ #
import json

#-----------------------------  DATA LAYER  -------------------------------- #
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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

#----------------------------- PRESENTATION LAYER  ------------------------- #
"""
Student-PyQ,3/4/25, added a functions define area, 
                    modified to organize into IO, FileProcessor classes.
"""
#start of function define
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    Student-PyQ,3/4/25, created
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function prints error message.
        Student-PyQ,3/4/25, created
        :param message: Custom error message.
        :param error: Exception class.
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function simply prints the menu options 1 - 4.
        Student-PyQ,3/4/25, created
        :param menu: String formatted menu.
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function gets menu option selection.
        Student-PyQ,3/4/25, created
        :return: User input value.
        """
        return input("What would you like to do: ")

    @staticmethod
    def output_student_course(student_data: list):
        """
        This function displays the list of students registered.
        Student-PyQ,3/4/25, created
        :param student_data: List of students.
        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets new student registration details and saves
        to details to a current list of student data.
        Student-PyQ,3/4/25, created
        :param student_data: Current list of student data.
        :return: student_data list of registered students.
        """
        global student_first_name
        global student_last_name
        global course_name

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data.append({"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name})
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            #print(e)  # Prints the custom message
            #print("-- Technical Error Message -- ")
            #print(e.__doc__)
            #print(e.__str__())
            IO.output_error_messages(message="", error=e)
        except Exception as e:
            #print("Error: There was a problem with your entered data.")
            #print("-- Technical Error Message -- ")
            #print(e.__doc__)
            #print(e.__str__())
            IO.output_error_messages(message="There was a problem with your entered data.", error=e)
        return student_data

#----------------------------- PROCESSING LAYER  --------------------------- #
"""
Student-PyQ,3/4/25, created FileProcessing class for encapsulating functions
"""
class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads from a JSON file.
        Student-PyQ,3/4/25, created.
        :param file_name: JSON file name.
        :param student_data: List to load JSON file data into.
        :return: student_data list of dictionary
        """
        global file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            #print("Error: There was a problem with reading the file.")
            #print("Please check that the file exists and that it is in a json format.")
            #print("-- Technical Error Message -- ")
            #print(e.__doc__)
            #print(e.__str__())
            IO.output_error_messages(message="There was a problem with reading the file.\n"
                                             "Please check that the file exists and that "
                                             "it is in a json format.",error=e)
        finally:
            if file is None:
                file = open(file_name, "r")
                file.close()
            else:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes student data to JSON file using dump method.
        Displays list of student data saved to JSON file.
        Student-PyQ,3/4/25, created.
        :param file_name: JSON file name.
        :param student_data: List representing student data.
        :return: None
        """
        global file

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if not file.closed:
                file.close()
            #print("Error: There was a problem with writing to the file.")
            #print("Please check that the file is not open by another program.")
            #print("-- Technical Error Message -- ")
            #print(e.__doc__)
            #print(e.__str__())
            IO.output_error_messages(message="There was a problem with writing to the file.\n"
                                             "Please check that the file is not open by "
                                             "another program.", error=e)
        finally:
            if file is None:
                file = open(file_name, "w")
                file.close()
            else:
                file.close()


#end of function define
#----------------------------- MAIN SCRIPT BODY  --------------------------- #
# Beginning of the main body of this script
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
"""
Student-PyQ,3/4/25, new function read_data_from_file(file_name: str, student_data: list)
"""
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    """
    Student-PyQ,3/4/25, use new functions
    """
    #print(MENU)
    #menu_choice = input("What would you like to do: ")
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        """
        Student-PyQ,3/4/25, use new function input_student_data(student_data: list)
        """
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        """
        Student-PyQ,3/4/25, use new function output_student_course(student_data: list)
        """
        # Process the data to create and display a custom message
        IO.output_student_course(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        """
           Student-PyQ,3/4/25, use function write_data_to_file(file_name: str, student_data: list)
        """
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
