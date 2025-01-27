# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 1 - Chapter 2
# Exercise 5: Write a program which prompts the user for a Celsius temperature,
#             convert the temperature to Fahrenheit, and print out the
#             converted temperature.

# ----- Section 1 - Get Input -----
print('This program converts a Celsius temperature to a Fahrenheit temperature.')
# Display a string to the user. Then have the user input the answer on the same line.
prompt_celsius_temperature = 'Pleas Enter a Celsius Temperature: '
# The input is saved as a string in variable called string_celsius_temperature
string_celsius_temperature = input(prompt_celsius_temperature)
# ----- Section 1 - Get Input -----

# ----- Section 2 - Perform Conversion -----
# convert input string values to float values
float_celsius_temperature = float(string_celsius_temperature)
# multiply the value stored in variable float_input_hours and float_input_rate
# and save the product in the variable called float_pay_rate
# float_pay_rate = float_input_hours * float_input_rate
float_fahrenheit_temperature = (float_celsius_temperature * 9/5) + 32
# ----- Section 2 - Perform Conversion -----

# ----- Section 3 - Display Output -----
# Display Fahrenheit Temperature
print(string_celsius_temperature, 'Degrees Celsius converted to Fahrenheit is', float_fahrenheit_temperature, 'Degrees Fahrenheit')
# ----- Section 3 - Display Output -----
