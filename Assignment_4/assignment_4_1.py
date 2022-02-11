# assignment_4_1

# Exercise 8:

# 1
print("~~~~ 1 ~~~~")


def func():
    print("Hello World")


func()

# 2
print("~~~~ 2 ~~~~")


def func1(name):
    print(f"Hi My name is {name}")


func1("Google")

# 3
print("~~~~ 3 ~~~~")


def func3(x, y, z):
    if z is True:
        return x
    else:
        return y


z = False
print(func3("hello", "goodbye", z))


# 4
print("~~~~ 4 ~~~~")


def func4(x, y):
    return x * y


print(func4(5, 4))

# 5
print("~~~~ 5 ~~~~")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(6))

# 6
print("~~~~ 6 ~~~~")


def is_greater(num_1, num_2):
    if num_1 > num_2:
        return True
    else:
        return False


print(is_greater(8, 5))

# 7
print("~~~~ 7 ~~~~")


def sum_of(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum


print(sum_of(5, 10, 5))

# 8
print("~~~~ 8 ~~~~")


def only_even(*args):
    answer_list = []
    for num in args:
        if num % 2 == 0:
            answer_list.append(num)
    return answer_list


print(only_even(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 9
print("~~~~ 9 ~~~~")


def upper_and_lower(my_string):
    answer_string = ""
    for i, char in enumerate(my_string):
        if i % 2 == 0:
            answer_string += char.upper()
        else:
            answer_string += char.lower()
    return answer_string


print(upper_and_lower("Stephen"))

# 10
print("~~~~ 10 ~~~~")


def any_odds(number_1, number_2):
    if number_1 % 2 != 0 or number_2 % 2 != 0:
        return max(number_1, number_2)
    else:
        return min(number_1, number_2)


print(any_odds(6, 9))

# 11
print("~~~~ 11 ~~~~")


def start_with_same_letter(string_1, string_2):
    if string_1[0].lower() == string_2[0].lower():
        return True
    else:
        return False


print(start_with_same_letter("Stephen", "start"))

# 12
print("~~~~ 12 ~~~~")


def double_otherside_7(value):
    distance = (7 - value) * 2
    return distance + 7


print(double_otherside_7(9))


# 13
print("~~~~ 13 ~~~~")


def first_and_fourth(my_string):
    answer_string = ""
    for i, char in enumerate(my_string):
        if i == 0 or i == 3:
            answer_string += char.upper()
        else:
            answer_string += char
    return answer_string


print(first_and_fourth("stephen"))
