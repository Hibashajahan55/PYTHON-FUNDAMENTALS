# Exercise 1
# Write Python code that prints your name, student number and email address.

print("Bob")
print("ST1001")
print("bob@gmail.com")

# Exercise 2
# Write Python code that prints your name, student number and email address using escape sequences.
print("Bob\nST1001\nbob@gmail.com")

# Exercise 3
# Write Python code that add, subtract, multiply and divide the two numbers. You can use the two numbers 14 and 7.

num1 = 14
num2 = 7
# ADDITION
print(f"{num1} + {num2} = {num1 + num2}")
# SUBSTRACTION
print(f"{num1} - {num2} = {num1 - num2}")
# MULTIPLICATION
print(f"{num1} * {num2} = {num1 * num2}")
# DIVISION
print(f"{num1} / {num2} = {num1 / num2}")

# Exercise 4
# Write Python code that displays the numbers from 1 to 5 as steps.
print("""1\n2\n3\n4\n5""")
# or
for i in range(1, 6):
    print(i)

# Exercise 5
# Write Python code that outputs the following sentence (including the quotation marks and line break) to the screen:
'''
"SDK" stands for "Software Development Kit", whereas
"IDE" stands for "Integrated Development Environment".
'''

print('"SDK" stands for "Software Development Kit", whereas\n"IDE" stands for "Integrated Development Environment".')

# Exercise 6
# Practice and check the output

print("python is an \"awesome\" language.")
# python is an "awesome" language.

print("python\n\t2023")
# python
# 	2023

print('I\'m from Entri.\b')
# I'm from Entri

print("\65")
# 5

print("\x65")
#  e

print("Entri", "2023", sep="\n")
# Entri
# 2023

print("Entri", "2023", sep="\b")
# Entr2023

print("Entri", "2023", sep="*", end="\b\b\b\b")
# Entri*

print()

# Exercise 7
# Define the variables below. Print the types of each variable. What is the sum of your variables? (Hint: use a type conversion function.) What datatype is the sum?
# num=23
# textnum="57"
# decimal=98.3

num = 23
textnum = "57"
decimal = 98.3

print("Type of num:", type(num))
print("Type of textnum:", type(textnum))
print("Type of decimal:", type(decimal))
# Type of num: <class 'int'>
# Type of textnum: <class 'str'>
# Type of decimal: <class 'float'>
sum_of_variables = num + int(textnum) + decimal
print("Sum of variables:", sum_of_variables)
print("Type of sum:", type(sum_of_variables))
# Sum of variables: 178.3
# Type of sum: <class 'float'>


# Exercise 8
# calculate the number of minutes in a year using variables for each unit of time.
# print a statement that describes what your code does also.
# Create three variables to store no of days in a year, minute in a hour, hours in a day,
# then calculate the total minutes in a year and print the values
# (hint) total number of minutes in an year =No.of days in an year * Hours in a day * Minutes in an hour

days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

total_minutes = days_in_year * hours_in_day * minutes_in_hour

print("days_in_year = 365\nhours_in_day = 24\nminutes_in_hour = 60\nTotal number of minutes in an year = No.of days in an year * Hours in a day * Minutes in an hour")
print(f"Total minutes in a year = {days_in_year} * {hours_in_day} * {minutes_in_hour} = {total_minutes}")

# Exercise 9
# Write Python code that asks the user to enter his/her name and then output/prints his/her name with a greeting.
# An example runs of the program:
# Please enter you name: Tony
# Hi Tony, welcome to Python programming :)


name = input("Enter your name: ")
print("Hi " + name + ", welcome to Python programming")

# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX£XXX are $XXX

print("Pounds To Dollars Conversion")
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * 1.25

print("£" + str(pounds) + " are $" + str(dollars))