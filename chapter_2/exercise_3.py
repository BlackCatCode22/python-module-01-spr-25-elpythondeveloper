# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 1 - Chapter 2
# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

# ----- Section 1 - Get Input -----
# Display a string to the user. Then have the user input the answer on the same line.
prompt_hours = 'Enter Hours: '
# The input is saved as a string in variable called string_input_hours
string_input_hours = input(prompt_hours)
# Display a string to the user. Then have the user input the answer on the same line.
prompt_rate = 'Enter Rate: '
# The input is saved as a string in variable called string_input_rate
string_input_rate = input(prompt_rate)
# ----- Section 1 - Get Input -----

# ----- Section 2 - Perform Calculation -----
# convert input string values to float values
float_input_hours = float(string_input_hours)
float_input_rate = float(string_input_rate)
# multiply the value stored in variable float_input_hours and float_input_rate
# and save the product in the variable called float_pay_rate
float_pay_rate = float_input_hours * float_input_rate
# ----- Section 2 - Perform Calculation -----

# ----- Section 3 - Display Output -----
# Display the string Pay: followed by the value stored in variable float_pay_rate in the console
print("Pay:", float_pay_rate)
# ----- Section 3 - Display Output -----
