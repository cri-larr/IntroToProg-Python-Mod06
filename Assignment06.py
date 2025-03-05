# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: Cristina Larrea, 3/4/2025, created script
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the program's data
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# Processing --------------------------------------- #
class FileProcessor:


    """
A collection of processing functions that work with Json files

ChangeLog:
Cristina, 3/4/20205, created first class
Cristina, 3/4/20205, added two functions to interact with JSON data
Cristina, 3/4/20205, included exception handling to the functions

    """

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # global file
        # global students

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation functions that manage user input and output

    ChangeLog:
    Cristina,3.4.2025,Created Class
    Cristina,3.4.2025, Added a function to display menu details
    Cristina,3.4.2025, Added a function to request inputs from user
    Cristina,3.4.2025,Added a function to display custom error messages and course details to user
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user
        ChangeLog:
        Cristina,3.4.2025,Created function
        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of choices to the user
        ChangeLog:
        Cristina,3.4.2025,Created function
        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
        Cristina, 3.4.2025, Added exception handling if user provides invalid number
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog:
        Cristina,3.4.2025,Created function
        Cristina,3.4.2025,added error handling if invalid data type is inputted
        :return: incremental student data
        """

        try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                course_name = input("Please enter the name of the course: ")
                student_data = {"FirstName": student_first_name,
                                    "LastName": student_last_name,
                                    "CourseName": course_name}
                students.append(student_data)
                print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
                print(e)  # Prints the custom message
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())
        except Exception as e:
                print("Error: There was a problem with your entered data.")
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())


def output_student_courses(student_data: list):
    """ This function displays student data captured

    ChangeLog:
    Cristina, 3.4.2025,Created function to display student details
    :return: None
    """
    # Process the data to create and display a custom message

    print("-" * 50)
    for student in student_data:
        print(f'Student {student["FirstName"]} '
              f'{student["LastName"]} is enrolled in {student["CourseName"]}')
    print("-" * 50)



#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        output_student_courses(student_data=students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        IO.input_student_data(student_data=students)
        output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        print('the program has ended, thank you')
        break  # out of the while loop
