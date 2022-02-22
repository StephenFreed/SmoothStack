import os
import time
import subprocess
import validation_functions as validate
import parse_excel_functions as pe
import file_functions as ff
import logging

# todo check if file is infiles_processed or error_files

# structures logging formatting to log_file
logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S %m-%d-%Y",
    filename="/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/log_file.txt"
)

# pulls in list of file names from target excel file directory
excel_directory = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/"
excel_file_list = os.listdir(excel_directory)  # list of file names as str

# builds list of available files from that directory to diplay to user
input_display_list_of_files = "~~~ Files To Parse ~~~\n~~~~~~~~~~~~~~~~~~~~~~\n"

# if directory empty shows different promt to user
if len(excel_file_list) < 1:
    input_display_list_of_files = (
                                   "~~~ There Are No Files In The Directory To Parse ~~~\n"
                                   "Add Files To excel_file Directory\n"
                                   "~~~~~~~~~~~~~~~~~~~~~~\n"
                                   "\nChoose 0 To Quit Application"
                                   )

else:
    # loops through file names to print
    for file_name in excel_file_list:
        input_display_list_of_files += f"File: {file_name}\n"

    input_display_list_of_files += (
                                    "~~~~~~~~~~~~~~~~~~~~~~\n"
                                    "\nChoose 0 To Quit Application"
                                    "\nChoose 1 To Run Application\n"
                                    )

# asks user to run or quit application
selection = True
while selection:
    try:

        # asks for user to run(1) or quit(0) application after listing files
        file_selection_number = int(input(
            f"\n--- Excel Application ---\n\n{input_display_list_of_files}\nEnter Number: ")
        )

        # 0 quits application
        if file_selection_number == 0:
            logging.info("Application Was Successfully Closed")
            print("\nExiting Excel Application...\n\n~~~~ Successfully Closed Application ~~~~")
            # terminates while
            selection = False

        # check if number is 0 or 1
        elif file_selection_number < 0 or file_selection_number > 1:
            logging.error("Selected Invalid Number To Start or Quit Application")
            print("\n(Error!) Please Select 0 or 1...")

        else:

            # terminates while
            selection = False

            # loops through files in excel_files directory
            for file_name_2 in excel_file_list:

                # validates file name
                print(f"Validating: {file_name_2}")
                is_valid_file = validate.is_valid_file_name(file_name_2)

                # if file name is valid runs parsing function on excel file
                if is_valid_file == "valid_file_name":
                    logging.info(f"Parsing Valid File Name: {file_name_2}")
                    print(f"Parsing Valid File Name: {file_name_2}")
                    pe.parse_excel_data(file_name_2)
                    # terminates while

                else:
                    # logs and prints to user
                    logging.error("File Name Is Not Valid")
                    print(f"\n(Error!) File name is not valid\nMoving {file_name_2} Into invalid_name Directory")
                    # then moves file to error_files/invalid_name dir / adds name to error_files.txt
                    ff.move_invalid_filename(file_name_2)

    except IndexError:  # out of range
        logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:  # noqa all other problems
        logging.error("There Was A Problem Running The Application")
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")

    else:

        print("\n~ Application Was Successful ~")

        print("~~~~~~~~~~~~~~~~~~~~~~\n ~ Opening Log File ~\n~~~~~~~~~~~~~~~~~~~~~~")

        # time.sleep(1)
        # subprocess.call(["open", "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/log_file.txt"])
