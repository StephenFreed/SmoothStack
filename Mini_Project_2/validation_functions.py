import re
import logging


# validation function to validate file name is in correct format to parse from
def is_valid_file_name(file_name: str) -> str:

    """
    Validation function to validate file name is in correct format to parse
    Valid Format: "expedia_report_monthly_{month in lowercase}_{4 digit year}.xlsx"
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
