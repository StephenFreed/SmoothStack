import re
import time
import datetime
import subprocess
import openpyxl
import logging


# custom error to handle if anything fails during parsing of excel file
# error is called after known handled exceptions so the program does not crash
# errors are logged and then printed to the user for information on what happened
class ProgramError(Exception):
    pass


# validate datetime cell and validate month spelled out
def validate_datetime(cell_string) -> bool:
    return True
    date_format = "%Y-%m-%d %H:%M:%S"
    try:
        # checks if cell is not empty and that date is in correct format
        if cell_obj.value is not None and datetime.datetime.strptime(cell_string, date_format):
            date_and_row = (cell_string, row_number)
            parsed_date_list.append(date_and_row)
    # passes if strptime function fails on invalid date format
    except:  # noqa
        pass


def validate_month_string(cell_string) -> bool:
    return True


def parse_excel_data(file_name_to_parse: str):

    """
    Parses data based on file name input. Looks for month and year.
    Returns data from that month and year in the excel file.
    """

    # try block if anything goes wrong with parsing logs and displays to User
    # this keeps from program reporting wrong details at the end
    try:

        # splits file name on "_" and "." into list to validate
        file_name_list = re.split('_|\\.', file_name_to_parse)
        month_from_filename = file_name_list[3]
        year_from_filename = file_name_list[4]

        # loads excel workbook
        wb_obj = openpyxl.load_workbook(
            "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_2/excel_files/{}".format(file_name_to_parse)
            )

        # gets list of sheets in workbook
        if "VOC Rolling MoM" in wb_obj.sheetnames:
            # sets sheet of workbook
            sheet_obj = wb_obj["VOC Rolling MoM"]
            print("sheet was found")
            print(sheet_obj['B1'].value)
            print(sheet_obj['E1'].value)

        else:
            logging.error("'VOC Rolling MoM' Sheet Was Not Found In Workbook")
            print("\n(ERROR) 'VOC Rolling MoM' Sheet Was Not Found In Workbook")
            raise ProgramError



        # find column number
        # loop through top row looking for proper date(2 choices)
        # look for "Full Name" or parse date 01 index is month 0 index is year
        column_to_parse = None
        m_column = sheet_obj.max_column  # type: ignore
        for column_number in range(1, m_column + 1):
            try:
                header_cell_obj = sheet_obj.cell(row=1, column=column_number)  # type: ignore
                cell_string = str(header_cell_obj.value).strip()
                datetime_result = validate_datetime(cell_string)
                month_string_result = validate_month_string(cell_string)
                if datetime_result is True or month_string_result is True:
                    column_to_parse = column_number

            except: # noqa
                logging.error("Error While Building Header,Column List In parse_excel_functions.py")
                print("\n(ERROR) Error While Building Header,Column List In parse_excel_functions.py")
                raise ProgramError
        if column_to_parse == None:
            pass
            # todo throw error month not found


        # loop through first row looking for correct rows(3 choices)
        # build tuple (row_name, row_number)
        row_to_parse = []
        m_row = sheet_obj.max_row  # type: ignore // gets max row number
        for row_number in range(1, m_row + 1):
            cell_obj = sheet_obj.cell(row=row_number, column=1)  # type: ignore
            cell_string = str(cell_obj.value).strip()  # object to string
            try:
                if cell_obj.value is None:
                    continue

                split_string_list = re.split(' ', date)  # split string into list on space
                if split_string_list[0].title() == "Promoters" or 
                split_string_list[0].title() == "Passives" or
            split_string_list[0].title() == "Dectractors":
                row_to_parse.append((split_string_list[0].title(), row_number))

            # passes if strptime function fails on invalid date format
            except:  # noqa
                pass

        if len(row_to_parse) != 3:
            # todo error missing row fields





        # builds logging output for successful parsing of data
        list_of_worksheets = wb_obj.sheetnames  # get workbook list of worksheets
        successful_log_string = ""
        successful_log_string += "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        successful_log_string += "Successfully Parsed Excel File: {}\n".format(file_name_to_parse)
        successful_log_string += "Data From Worksheet: {}\n".format(list_of_worksheets[0])
        successful_log_string += (
                                  "~~~ For the Month of {} in {} ~~~\n"
                                  .format(month_from_filename.capitalize(), year_from_filename)
                                  )

        # loops through target row concatenating header and row info
        for header, column_number in header_and_column_list:  # unpacks tuple
            try:
                target_row_column_cell_obj = sheet_obj.cell(row=row_of_info, column=column_number)  # type: ignore
                target_row_column_cell = str(target_row_column_cell_obj.value).strip()
                if target_row_column_cell[:2] == "0.":  # check if % in cell
                    target_row_column_cell_float = float(target_row_column_cell)
                    successful_log_string += "{}: {:.2%}\n".format(header, target_row_column_cell_float)
                else:
                    target_row_column_cell_int = int(target_row_column_cell)
                    successful_log_string += "{}: {}\n".format(header, target_row_column_cell_int)
            except: # noqa
                logging.error("Error While Building successful_log_string In parse_excel_functions.py")
                print("\n(ERROR) Error While Building successful_log_string In parse_excel_functions.py")
                raise ProgramError

        successful_log_string += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    except ProgramError:
        logging.error("A Known Exception Was Handled | Application Could Not Finish")
        print("The Known Exception Above Was Handled ^^^\nApplication Could Not Finish\nPlease Check Log File...")

    except: # noqa
        logging.error("The Program Could Not Get Excel Data Successfully")
        print("The Program Could Not Get Excel Data Successfully\nTry Another File\nClosed Application...")

    # displays parsed data to user and logs it if there were no exceptions
    else:

        print("\n~ Application Was Successful ~")

        # log and print parse info
        logging.info(successful_log_string)
        print(successful_log_string)

        logging.info("Application Successfully Ran")

        print("~~~~~~~~~~~~~~~~~~~~~~\n ~ Opening Log File ~\n~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(1)
        subprocess.call(["open", "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/logging/log_file.txt"])
