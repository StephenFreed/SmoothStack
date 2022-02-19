import os
import validation_functions as validate
import parse_excel_functions as pe
import logging

# structures logging formatting to log_file
logging.basicConfig(
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S %m-%d-%Y",
    filename="/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/logging/log_file.txt"
)

# pulls in list of file names from target excel file directory
excel_directory = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/"
excel_file_list = os.listdir(excel_directory)  # list of file names as str

# builds list of available files from that directory to diplay to user

input_display_list_of_files = "~~~ Files To Parse ~~~\n~~~~~~~~~~~~~~~~~~~~~~\n"

if len(excel_file_list) < 1:
    input_display_list_of_files = (
                                   "There Are No Files In The Directory To Parse...\n"
                                   "Add Files To excel_file Directory"
                                   "~~~~~~~~~~~~~~~~~~~~~~\n"
                                   "\nChoose 0 To Quit Application"
                                   )

else:
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

        # calls is_valid_file_name function in validate module
        # if invalid logs error to log file in validation_functions module
        # returns custom log error to print to user if invalid
        # then moves file to error dir/continues with list of files
        # if valid runs parse_excel_data function from parse_excel module
        else:

            for file_name_2 in excel_file_list:

                is_valid_file = validate.is_valid_file_name(file_name_2)
                if is_valid_file != "valid_file_name":
                    print(is_valid_file)

                    # move invalid file name to error_files/invalid_name dir
                    try:
                        excel_file_source = (
                        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{file_name_2}"  # noqa
                        )
                        excel_file_dest = (
                        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/error_files/invalid_name/{file_name_2}"  # noqa
                        )
                        os.replace(excel_file_source, excel_file_dest)
                        print(f"{file_name_2} Was Moved To error_files/invalid_name Directory")

                    # destination is a directory
                    except IsADirectoryError:
                        print("Source is a file but destination is a directory.")

                    # If source is a directory
                    # but destination is a file
                    except NotADirectoryError:
                        print("Source is a directory but destination is a file.")

                    # For permission related errors
                    except PermissionError:
                        print("Operation not permitted.")

                    # For other errors
                    except OSError as error:
                        print(error)

                # if file name is valid runs parsing function on excel file
                # parsing functions in module parse_excel_functions
                else:
                    pe.parse_excel_data(file_name_2)
                    # terminates while
                    selection = False

    except IndexError:  # out of range
        logging.error("Selected File Number Was Out Of Range Of Choices")
        print("\n(Error!) Please Select Numbers 0 or 1...")

    except Exception as e:  # noqa all other problems
        logging.error("Selected File Choice Was Not A Valid Choice")
        print("\n(Error!) Selected File Choice Was Not A Valid Choice\nSelect A Valid Number...")
        print(e)  # used to troubleshoot
