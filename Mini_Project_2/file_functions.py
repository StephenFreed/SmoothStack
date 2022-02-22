import os


def move_invalid_filename(file_name_2):
    # move invalid file name to error_files/invalid_name directory
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


def move_invalid_file(file_name_to_parse):
    pass


def move_processed_file(file_name_to_parse):
    try:
        excel_file_source = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{file_name_to_parse}"  # noqa
        )
        excel_file_dest = (
        f"/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/logging/processed_files/{file_name_to_parse}"  # noqa
        )
        os.replace(excel_file_source, excel_file_dest)
        print(f"{file_name_to_parse} Was Moved To error_files/invalid_name Directory")

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
