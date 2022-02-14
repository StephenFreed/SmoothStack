import os
import subprocess
import time
import validation_functions as validate
import parse_excel_functions as pe
import logging

# log file instead of txt

# structures logging formatting to log_file
logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S %m-%d-%Y",
    filename="/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/log_file.txt"
)


# pulls in list of file names from target excel file directory
excel_directory = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/Excel_Files/"
excel_file_list = os.listdir(excel_directory)


# builds list of available files from that directory to diplay as choices to user
input_display_list_of_files = "Choose 0 To Quit Application\n"
for i, file_name in enumerate(excel_file_list):
    input_display_list_of_files += f"Choose {i+1} for: {file_name}\n"


# asks to select file to parse data from
selection = True
while selection:
    try:

        # asks for user to choose from list of options / lists those options
        file_selection_number = int(input(
            f"\n-- Please Select A File To Parse --\n{input_display_list_of_files}\nEnter Number: ")
        )

        # validation to make sure input selection is valid
        # 0 quits application
        if file_selection_number == 0:
            logging.info("Application Was Successfully Closed")
            print("\nExiting Parsing Application...\n~~~~ Successfully Closed Application ~~~~")
            # terminates while
            selection = False

        # checks if number is negative/can give false results(example list[-1])
        elif file_selection_number < 1:
            logging.error("Selected File Number Was Out Of Range Of Choices")
            print("\n(Error!) Please Select A Number Displayed...")

        # calls is_valid_file_name function in validate module
        # if invalid logs error and asks user to choose a valid file name
        # if valid runs parse_excel_data function from parse_excel module
        else:

            # calls is_valid_file from validate module on selected file
            # validation function in module validation_functions
            is_valid_file = validate.is_valid_file_name(excel_file_list[file_selection_number - 1])
            # checks if return is a valid file name/ if not asks user to chose again
            if is_valid_file != "valid_file_name":
                print(is_valid_file)

            # if file name is valid runs parsing function on excel file
            # parsing functions in module parse_excel_functions
            else:
                pe.parse_excel_data(excel_file_list[file_selection_number - 1])
                logging.info("Application Successfully Ran")
                print(f"\nCongratulations!\n\nYou Selected File: {excel_file_list[file_selection_number - 1]}\n")
                print("~~~~~~~~~~~~~~~~~~~~~~\n ~ Opening Log File ~\n~~~~~~~~~~~~~~~~~~~~~~")
                # terminates while
                selection = False

    # out of range
    except IndexError:
        logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select A Number Displayed...")

    # all other problems
    except Exception as e:
        logging.error("Selected File Choice Was Not A Valid Choice")
        print("\n(Error!) Selected File Choice Was Not A Valid Choice\nSelect A Valid Number...")
        print(e)


# time.sleep(1)
# subprocess.call(["open", "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/log_file.txt"])
