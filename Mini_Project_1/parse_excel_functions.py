import re
import datetime
import openpyxl
import logging

# if everything is valid parses data
def parse_excel_data(file_name_to_parse):

    # splits file name on "_" and "." into list to validate
    file_name_list = re.split('_|\\.', file_name_to_parse)
    month_from_filename = file_name_list[3]
    year_from_filename = file_name_list [4]

    # loads excel workbook
    wb_obj = openpyxl.load_workbook(
        "/Users/stephenfreed/Projects/SmoothStack/Mini_Project_1/Excel_Files/{}".format(file_name_to_parse)
    )
    # gets active sheet of workbook
    sheet_obj = wb_obj.active

    # build list of first colomn values and find row with matching month and year
    m_row = sheet_obj.max_row  # gets max row number
    # builds list of valid dates and the rows they were in
    parsed_date_list = []
    for row_number in range(1, m_row + 1):
        cell_obj = sheet_obj.cell(row=row_number, column=1)
        cell_string = str(cell_obj.value)  # object to string
        date_format = "%Y-%m-%d %H:%M:%S"
        # try:
        # checks if cell is not empty and that date is in correct format
        if cell_obj.value is not None and datetime.datetime.strptime(cell_string, date_format):
            # date_string = str(cell_obj.value)
            date_and_row = (cell_string, row_number)
            parsed_date_list.append(date_and_row)
        # except Exception as e:
            # pass
            # print(e)

    # print("Parsed Date List: \n {}".format(parsed_date_list))

    # loops through parsed date_list and finds row we need to parse
    row_of_info = None
    for date, row in parsed_date_list:
        try:
            split_date_list = re.split('-| ', date) # split date into list
            # print(split_date_list)
            month_to_number_dict = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06", "july": "07", "august": "08", "september": "9", "october": "10", "november": "11", "december": "11"}
            # print("{} - {}".format(split_date_list[0], year_from_filename))
            # print("{} - {}".format(split_date_list[1], month_to_number_dict[month_from_filename]))
            if split_date_list[0] == year_from_filename and split_date_list[1] == month_to_number_dict[month_from_filename]:
                row_of_info = row
                # print("The row we need info from is: {}".format(row))
        except:
            # todo something went wrong
            print("something went wrong")

    # return row info
    # get column row header numbers to names
    list_of_worksheets = wb_obj.sheetnames
    # print(list_of_worksheets)

    # get header info
    header_and_column_list = []
    m_column = sheet_obj.max_column
    for column_number in range(1, m_column + 1):
        try:
            cell_obj_2 = sheet_obj.cell(row=1, column=column_number)
            cell_string = str(cell_obj_2.value).strip()
            header_and_column_number = (cell_string, column_number)
            if cell_obj_2.value is not None:
                header_and_column_list.append(header_and_column_number)
        except Exception as e:
            print("somethign went wrong 404")
            print(e)

    print(header_and_column_list)
# Calls Offered: 16,91
# Abandon after 30s : 2.32%
# FCR : 86.50%
# DSAT :  14.20%
# CSAT : 78.30%
    successful_log_string = "\n"
    successful_log_string += "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    successful_log_string += "This is from worksheet {}\n".format(list_of_worksheets[0])
    successful_log_string += "From Excel file {}\n".format(file_name_to_parse)

    for header, column_number in header_and_column_list:
        try:
            cell_obj_3 = sheet_obj.cell(row=row_of_info , column=column_number)
            successful_log_string += f"{header}: {column_number}\n"
            # print(f"{header}-{column_number}")
        except Exception as e:
            print(e)

    successful_log_string += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    logging.info(successful_log_string)
    print(successful_log_string)
