import csv

# assignment_5_1


# function to calculate each inputs bmi / returns list of answers
def calculate_bmi(data_list) -> list:
    results_list = []
    for row in data_list:
        bmi = int(row[0]) / float((row[1]))**2

        if bmi < 18.5:
            results_list.append("under")
        elif 18.5 <= bmi < 25.0:
            results_list.append("normal")
        elif 25.0 <= bmi < 30.0:
            results_list.append("over")
        elif 30.0 <= bmi:
            results_list.append("obese")

    return results_list


# result of data parsed from txt file below
people_data_list = []

with open("/Users/stephenfreed/Projects/SmoothStack/Assignment_5/input_data.txt", "r") as input_file:
    reader = csv.reader(input_file)  # gets rows of txt file
    header = next(reader)  # skip header row (Input Data:)
    # gets number of people in input data / skips row / list -> [0] of list -> integer
    num_of_people = int(next(reader)[0])
    # loops to build clean list (strip white space)
    for row in reader:
        # converts list str to just str and splits on white space
        # this creates list of the two inputs to work with
        split_row_list = str(row[0]).split(" ")
        # cleans and appends new split list with people data to people_data_list
        stripped_row = []
        for elm in split_row_list:
            stripped_row.append(elm.strip())
        people_data_list.append(stripped_row)

# calls function on created people_data_list from txt file
bmi_results = calculate_bmi(people_data_list)

# print results to console
for result in bmi_results:
    print(result, end=" ")

# writes results to file with some formatting
with open("bmi_reults.txt", "w") as answer_file:
    answer_file.write("These are the BMI results...\n")
    for row in range(num_of_people):
        answer_row = f"Person {row+1} BMI Result: {bmi_results[row]}\n"
        answer_file.write(answer_row)
