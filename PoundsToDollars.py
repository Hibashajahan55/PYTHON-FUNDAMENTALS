# Exercise 10
# Name your file: PoundsToDollars.py
# Write a program that asks the user to enter an amount in pounds (£) and the program calculates and converts an amount in dollar ($)
# An example runs of the program:
# Please enter amount in pounds: XXX£XXX are $XXX

print("Pounds To Dollars Conversion")
pounds = float(input("Please enter amount in pounds: "))
dollars = pounds * 1.25

print("£" + str(pounds) + " are $" + str(dollars))