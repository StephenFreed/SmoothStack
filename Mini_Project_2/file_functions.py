import os
import shutil
import logging


# moves files into error_files/invalid_name and adds file name to error_files.txt
def move_invalid_filename(file_name_2):

    """
    Moves excel file that has been found to have invalid name to error_files/invalid_name directory
    Logs file name to error_files.txt
    """

    try:
        excel_file_source = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{file_name_2}"  # noqa
        )
        excel_file_dest = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/error_files/invalid_name/{file_name_2}"  # noqa
        )

        os.replace(excel_file_source, excel_file_dest)

        # adds file name to error_file.txt
        invalid_name_source = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/error_files/error_files.txt"
        with open(invalid_name_source, "a") as invalid_name_source:
            invalid_name_source.write(f"{file_name_2}\n")

    except Exception as e:
        print(e)
        logging.error("Problem Moving File To error_files/invalid_name Directory")
        print("\n(ERROR) Problem Moving File To error_files/invalid_name Directory")


# moves files into error_files/invalid_file and adds file name to error_files.txt
def move_invalid_file(file_name_to_parse):

    """
    Moves excel file that has been found to be invalid to error_files/invalid_file directory
    Logs file name to error_files.txt
    """

    try:
        excel_file_source = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{file_name_to_parse}"  # noqa
        )
        excel_file_dest = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/error_files/invalid_file/{file_name_to_parse}"  # noqa
        )

        os.replace(excel_file_source, excel_file_dest)

        # adds file name to error_file.txt
        invalid_name_source = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/error_files/error_files.txt"
        with open(invalid_name_source, "a") as invalid_name_source:
            invalid_name_source.write(f"{file_name_to_parse}\n")

    except Exception as e:
        print(e)
        logging.error("Problem Moving File To error_files/invalid_file Directory")
        print("\n(ERROR) Problem Moving File To error_files/invalid_file Directory")


# moves files into logging/processed_files and adds file name to files_processed.txt
def move_processed_file(file_name_to_parse):

    """
    Moves excel file that have been successfully processed to logging/processed_files directory
    Logs file name to files_processed.txt
    """

    try:
        excel_file_source = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{file_name_to_parse}"  # noqa
        )
        excel_file_dest = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/processed_files/{file_name_to_parse}"  # noqa
        )

        os.replace(excel_file_source, excel_file_dest)

        # adds file name to files_processed.txt
        processed_source = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/processed_files/files_processed.txt"  # noqa
        with open(processed_source, "a") as fp:
            fp.write(f"{file_name_to_parse}\n")

    except Exception as e:
        print(e)
        logging.error("Problem Moving File To logging/processed_files Directory")
        print("\n(ERROR) Problem Moving File To logging/processed_files Directory")


# move test files from exel_files_repo directory to excel_files directory
def move_excel_repo_files():

    repo_dir = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files_repo/"
    repo_files = os.listdir(repo_dir)
    for file_name in repo_files:
        full_file_path = os.path.join(repo_dir, file_name)
        if os.path.isfile(full_file_path):
            excel_dir = "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/"
            shutil.copy(full_file_path, excel_dir)
