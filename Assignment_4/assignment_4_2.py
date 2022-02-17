import csv

# holds list built below from csv
book_shop_list = []

try:
    with open("/Users/stephenfreed/Projects/SmoothStack/Assignment_4/accounting_list.csv", "r") as f:
        reader = csv.reader(f)  # gets rows of csv list
        header = next(reader)  # skip header row
        # loops to build clean list (strip whitespace)
        for row in reader:
            stripped_row = []
            for elm in row:
                stripped_row.append(elm.strip())
            book_shop_list.append(stripped_row)

except Exception as e:
    print("Problem Importing From CSV File")
    print(e)


# function to calculate tuple
def calc_product(row):
    # finds product from correct index of row
    product = float(row[3]) * float(row[4])
    # adds 10 if below 100
    if product < 100:
        product += 10
    # lambda sets floats to 2 decimal places
    rounded_float = lambda x: "{:.2f}".format(x)  # noqa
    return (int(row[0]), rounded_float(product))


# map to run function on every row of list
answer = map(calc_product, book_shop_list)
print(list(answer))
