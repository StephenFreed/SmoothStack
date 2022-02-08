import math

# assignment_1_2 questions

# 1
first_number = 50 + 50
second_number = 100 - 10
print(first_number + second_number)

# 2
print("¯¯|_(ツ)_/¯¯")
boolean_answer = 6 ** 6 == 6*6*6*6*6*6
print(boolean_answer)

# 3
print("Hello World : 10")

# 4
loan_size = int(input("What is the size of the loan?(example: 800000) : "))
interest_rate = float(input("What is your yearly interest rate percentage?(example: 6.0) : "))
length_in_months = int(input("How many months would you like to calculate for?(example: 103) : "))

# formula for calculating monthly payment
# answer = loan_size(monthly_interest_rate(1 + monthly_interest_rate)^length_in_months) / (((1+monthly_interest_rate)**length_in_months) - 1)

monthly_interest_rate = (interest_rate / 100) / 12
part_1 = loan_size*(monthly_interest_rate*((1+monthly_interest_rate)**length_in_months))
part_2 = (((1+monthly_interest_rate)**length_in_months) - 1)
answer = part_1 / part_2
print("Necessary Monthly Payment: {rounded_answer}".format(rounded_answer = math.ceil(answer)))
