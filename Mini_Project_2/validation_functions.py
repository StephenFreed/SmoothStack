import re
import logging


# validation function that validates file name is in correct format to parse from
def is_valid_file_name(file_name: str) -> str:

    """
    Validation function to validate file name is in correct format to parse from
    Valid Format: "expedia_report_monthly_{month in lowercase}_{4 digit year}.xlsx"
    Returns "valid_file_name" or error message to print to user
    Logs errors to logging/log_file.txt
    """

    # list of months to validat month
    list_of_months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    # splits file name on "_" and "." into list to validate
    file_name_list = re.split('_|\\.', file_name)
    print(file_name_list)

    # checks proper length
    if len(file_name_list) != 6:
        logging.error("File Chosen Was Formatted Improperly")
        return (
                f"\n(ERROR: Invalid File Format) For File: {file_name}\n"
                "Format: expedia_report_monthly_{full month in lowercase}_{4 digit year}.xlsx"
                )

    # checks for proper file extension
    elif file_name_list[5] != "xlsx":
        logging.error("File Chosen Is Not A '.xlsx' Excel File")
        return f"\n(ERROR: Invalid File Extension) For File: {file_name}\n Must End in: .xlsx"

    # checks for expedia_report
    elif file_name_list[0].lower() == "expedia" and file_name_list[1].lower() == "report":
        logging.error("File Chosen Does not have expedia_report In Name Where It should Be")
        return f"\n(ERROR: File Chosen Does not have expedia_report in Name Where It should Be"

    # checks for valid month
    elif list_of_months.count(file_name_list[3]) != 1:
        logging.error("File Chosen Has Month Incorrectly Formatted In Name")
        return (
                f"\n(ERROR: Month Invalid) For File: {file_name}\n"
                "Format: expedia_report_monthly_{{full month in lowercase}}_{{4 digit year}}.xlsx"
                )

    # checks the year is 4 digits and all numeric
    elif len(file_name_list[4]) != 4 or file_name_list[4].isnumeric() is False:
        logging.error("File Chosen Has Incorrect Date Formatting")
        return (
                f"\n(ERROR: Year Invalid) For File: {file_name}\n"
                "Format: expedia_report_monthly_{{month in lowercase}}_{{4 digit year}}.xlsx"
                )

    # returns is a valid file name
    else:
        return "valid_file_name"


# gets list of sheets in workbook and checks if correct sheet is present
def check_for_sheet(wb_obj) -> tuple:

    """
    Gets a list of sheet names from openpyxl workbook object
    Loops through that list looking for "VOC Rolling MoM"
    Returns tuple[0] - True for Found and False for not Found
    Return tuple[1] - string name of worksheet
    """

    # loops through worksheets to find target sheet and index in list
    for sheet_name in wb_obj.sheetnames:
        if sheet_name == "VOC Rolling MoM":
            return (True, sheet_name)

    # if not found logs error, prints to user and returns not found tuple info
    logging.error("'VOC Rolling MoM' Sheet Was Not Found In Workbook")
    print("\n(ERROR) 'VOC Rolling MoM' Sheet Was Not Found In Workbook")
    return(False, 99)


# validates if cell date(month and year) match data parsed from file name
def validate_datetime(cell_string, month_from_filename, year_from_filename) -> bool:

    """
    Valicates if cell string date in format: 2017-12-01 00:00:00
    Matches month and year parsed from file name
    """

    # month to number dict to varify month of date format: 2017-12-01 00:00:00
    month_to_number_dict = {
                        "january": "01",
                        "february": "02",
                        "march": "03",
                        "april": "04",
                        "may": "05",
                        "june": "06",
                        "july": "07",
                        "august": "08",
                        "september": "09",
                        "october": "10",
                        "november": "11",
                        "december": "12"
                    }

    # split date into list on "-" and space
    split_date_list = re.split('-| ', cell_string)

    # checks year and month match parsed data from file name
    if (
        split_date_list[0] == year_from_filename and
        split_date_list[1] == month_to_number_dict[month_from_filename]
         ):
        return True
    else:
        return False


# validates if cell date(month only) match data parsed from file name
def validate_month_string(cell_string, month_from_filename) -> bool:

    """
    Valicates if cell string in format: January (Month with no date)
    Matches month parsed from file name
    """

    # list of months to query from
    list_of_months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    # check if cell string is in valid month list / checks if cell string is equal to month in file name
    if list_of_months.count(cell_string.lower()) == 1 and month_from_filename.lower() == cell_string.lower():
        return True
    else:
        return False


# returns rating for specific row / rating is used to log and print to user
def check_row_rating(row_name, target_row_column_cell) -> str:

    """
    Uses the row name and target cell data to return a rating
    Used to log and print to user
    """

    if row_name == "Promoters":
        if int(target_row_column_cell) >= 200:
            return "Good (200 or Greater)"
        else:
            return "Bad (Lower than 200)"

    elif row_name == "Passives":
        if int(target_row_column_cell) >= 100:
            return "Good (100 or Greater)"
        else:
            return "Bad (Lower than 100)"

    elif row_name == "Dectractors":
        if int(target_row_column_cell) >= 100:
            return "Good (100 or Greater)"
        else:
            return "Bad (Lower than 100)"
    else:
        return "No Rating Found For Row"
