import os
import time
import subprocess
import validation_functions as validate
import parse_excel_functions as pe
import file_functions as ff
import logging


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

# if directory is empty shows different promt to user
if len(excel_file_list) < 1:
    input_display_list_of_files = (
                                   "~~~ There Are No Files In The Directory To Parse ~~~\n"
                                   "~~~ Add Files To excel_file Directory ~~~\n"
                                   "\nChoose 0 To Quit Application"
                                   )

else:
    # loops through file names to print to user
    for file_name in excel_file_list:
        input_display_list_of_files += f"File: {file_name}\n"

    input_display_list_of_files += (
                                    "~~~~~~~~~~~~~~~~~~~~~~\n"
                                    "\nChoose 0 To Quit Application"
                                    "\nChoose 1 To Run Application\n"
                                    )

# while loop to keep active until valid input or user quits
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

        # runs program
        else:

            # terminates while
            selection = False

            # loops through files in excel_files directory
            for file_name_2 in excel_file_list:

                # logs and prints to user
                logging.info(f"Validating: {file_name_2}")
                print(f"\n~~~ Validating: {file_name_2} ~~~")

                # checks if file name has been logged to error_files.txt
                # function prints to user and logs to log file if it has
                in_error_files = validate.contained_in_error_files(file_name_2)

                # checks if file name has been logged to files_processed.txt
                # function prints to user and logs to log file if it has
                in_processed_files = validate.contained_in_processed_files(file_name_2)

                # if either returns true continues to next file
                if in_error_files is True or in_processed_files is True:
                    continue

                # validates file name
                is_valid_file = validate.is_valid_file_name(file_name_2)

                # if file name is valid runs parsing function on excel file
                if is_valid_file == "valid_file_name":
                    logging.info("Parsing Valid File Name...")
                    print("Parsing Valid File Name...")
                    pe.parse_excel_data(file_name_2)

                else:
                    # logs and prints to user
                    logging.info(f"Moving {file_name_2} Into invalid_name Directory")
                    print(is_valid_file)
                    print("\n(Error!) Moving {} Into invalid_name Directory\n".format(file_name_2))
                    # then moves file to error_files/invalid_name dir / adds name to error_files.txt
                    ff.move_invalid_filename(file_name_2)

    except IndexError:  # out of range
        logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:
        logging.error("There Was A Problem Running The Application")
        print(e)
        print("\n(Error!) There Was A Problem Running The Application...")

    # runs if program runs with no unhandled exceptions
    else:

        print("\n~ Application Was Successful ~\n")

        print("~~~~~~~~~~~~~~~~~~~~~~\n ~ Opening Log File ~\n~~~~~~~~~~~~~~~~~~~~~~")

        time.sleep(1)
        subprocess.call(["open", "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/log_file.txt"])
