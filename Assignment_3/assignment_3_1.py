import random

# assignment_3_1 questions

# Exercise 7:

# 1
print("~~~~ 1 ~~~~")

answer = ""
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        answer += f"{number}, "
print(answer[:-2])

# 2
print("~~~~ 2 ~~~~")

fahrenheit_number = 32
celsius_number = 27

# fahrenheit to celsius
celsius_conversion = (fahrenheit_number - 32) * (5/9)
print(f"{fahrenheit_number} fahrenheit is {celsius_conversion} celcius.")

# celcius to fahrenheit
fahrenheit_conversion = (celsius_number * (9/5) + 32)
print(f"{celsius_number} celcius is {fahrenheit_conversion} fahrenheit.")

# 3
print("~~~~ 3 ~~~~")

guess = True
while guess:
    try:
        random_number = random.randint(1, 9)
        random_guessed_number = int(input("Guess a whole number from 1-9:(Enter 0 To Quit) "))
        if random_guessed_number == 0:
            print("You quit playing...")
            guess = False
        elif random_number > random_guessed_number:
            print(f"{random_guessed_number} is less than {random_number}. Try again: ")
        elif random_number < random_guessed_number:
            print(f"{random_guessed_number} is more than {random_number}. Try again: ")
        else:
            print(f"You guessed the correct random number {random_number}")
            guess = False
    except:
        print("Please enter an integer: ")

# 4 and 5
print("~~~~ 4 and 5 ~~~~")

rows = 5
for row in range(rows):
    for asterisk in range(row+1):
        print("*", end=" ")
    print("\r")

for row in range(rows, 0, -1):
    for asterisk in range(row-1):
        print("*", end=" ")
    print("\r")

# 6
print("~~~~ 6 ~~~~")

word_entered = input("Enter a word: ")
print(word_entered[::-1])

# 7
print("~~~~ 7 ~~~~")

even_numbers = 0
odd_numbers = 0

my_boolean = True
while my_boolean:
    try:
        comma_seperated_numbers = input("Enter List of Comma-Seperated Numbers: ").replace(" ", "") # strips white space
        split_list = comma_seperated_numbers.split(",")
        for num in split_list:
            if (int(num) % 2 == 0):
                even_numbers += 1
            else:
                odd_numbers += 1
        print(f"There are {even_numbers} even numbers and {odd_numbers} odd numbers.")
        my_boolean = False
    except:
        print("Please enter only integers...")

# 8
print("~~~~ 8 ~~~~")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for element in datalist:
    print(f"{element} is of type {type(element)}.")

# 9
print("~~~~ 9 ~~~~")

for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i, end=" ")
