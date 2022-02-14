import re
import logging

# check to make sure file name is valid
def is_valid_file_name(file_name):
    """
    Validation Function
    """
    list_of_months =["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    file_name_list = re.split('_|\\.', file_name) # split file name into list
    if len(file_name_list) != 6:
        logging.error("File Chosen Was Formated Improperly")
        return "\n(ERROR: Invalid File Format) Formate expedia_report_monthly_{month in lowercase}_{4 digit year}.xlsx"
    elif file_name_list[5] != "xlsx":
        logging.error("File Chosen Is Not A '.xlsx' Excel File")
        return "\n(ERROR: Invalid File Extension) File Must End in: .xlsx"
    elif list_of_months.count(file_name_list[3]) != 1:
        logging.error("File Chosen Month Incorrectly Formated In Name")
        return "\n(ERROR: Month Invalid) Format expedia_report_monthly_{month in lowercase}_{4 digit year}.xlsx "
    elif len(file_name_list[4]) != 4 or file_name_list[4].isnumeric() is False:
        logging.error("File Chosen Has Incorred Date Formatting")
        return "\n(ERROR: Year Invalid) Format expedia_report_monthly_{month in lowercase}_{4 digit year}.xlsx "
    else:
        return "correct"
