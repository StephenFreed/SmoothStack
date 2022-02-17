# assignment_2_2 questions

# Exercise 4

# 1
print("~~~~ 1 ~~~~")
mixed_list = [5, "Something", 10.5]
print(mixed_list)

# 2
print("~~~~ 2 ~~~~")
nested_list = [1, 1, [1, 2]]
print(nested_list[2][1])

# 3
print("~~~~ 3 ~~~~")
list_3 = ["a", "b", "c"]
print(list_3[1:])

# 4
print("~~~~ 4 ~~~~")
weekday_dict = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saterday": 7
}
print(weekday_dict)

# 5
print("~~~~ 5 ~~~~")
# answer is 2
print("answer is 2")
D = {"k1": [1, 2, 3]}
print(D["k1"][1])

# 6
print("~~~~ 6 ~~~~")
# yes
print("answer is yes")
tuple_conversion = tuple([1, [2, 3]])
print(tuple_conversion)

# 7
print("~~~~ 7 ~~~~")
mississippi_set = set("Mississippi")
print(mississippi_set)

# 8
print("~~~~ 8 ~~~~")
# yes since there is not an "X" in the set
print("yes since there is not an 'X' in the set")
mississippi_set.add("X")
print(mississippi_set)

# 9
print("~~~~ 9 ~~~~")
# removes the 1
print(set([1, 1, 2, 3]))


# divisible by 7, but not 5
print("~~~~ divisible by 7, but not 5 ~~~~")
answer = ""
for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        answer += f"{number}, "
# return with last ", " stripped
print(answer[:-2])


# factorial
print("~~~~ factorial ~~~~")
while True:
    try:
        factorial_number = int(input("Enter Whole Number For Factorial: "))
    except:  # noqa
        print("This is not a whole number. Please enter number.")
    else:
        factorial_answer = 1
        for number in range(1, factorial_number + 1):
            factorial_answer *= number
        print(f"Factorial of {factorial_number} is: {factorial_answer}")
        break


# integral number dictionary
print("~~~~ integral number dictionary ~~~~")
while True:
    try:
        integral_number = int(input("Enter Number To Create Dictionary: "))
    except:  # noqa
        print("This is not a whole number. Please enter number.")
    else:
        integral_number_answer = {}
        for number in range(1, integral_number + 1):
            integral_number_answer[number] = number**2
        print(integral_number_answer)
        break


# generate list and tuple
print("~~~~ generate list and tuple ~~~~")
comma_seperated_numbers = input("Enter List of Comma-Seperated Numbers: ").replace(" ", "")  # strips white space
split_list = comma_seperated_numbers.split(",")
print(split_list)
print(tuple(split_list))


# class with methods
print("~~~~ Setting and Getting Object Attrabute String ~~~~")


class GetAndPrintString:
    def __init__(self):
        self.string = "You have not entered a string yet..."

    def set_string(self):
        string_input = input("Enter A String: ")
        self.string = string_input

    def get_string(self):
        print("This Objects String Is: " + self.string.upper())


# instanciates new object
my_new_object = GetAndPrintString()
# calls the set string method and sets string through console input
my_new_object.set_string()
# calls the get string to print to console in uppercase
my_new_object.get_string()
