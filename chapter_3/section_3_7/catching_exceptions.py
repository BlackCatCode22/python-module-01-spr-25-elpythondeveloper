# Chapter 3 - Conditional execution
# 3.7 Catching exceptions using try and except

# Example 1 - Convert a Fahrenheit Temperature to Celsius with try and except block
#
# Display a string to the user. Then have the user input the answer on the same line.
# The input is saved as a string in variable called string_celsius_temperature
inp = input('Enter Fahrenheit Temperature:')
try:
    # execute the items inside the try block
    # if there is an error then execution will to go the except block
    # convert the input string value to a float and save in variable called fahr
    fahr = float(inp)
    # perform the conversion calculation
    cel = (fahr - 32.0) * 5.0 / 9.0
    # display the celsius value stored in variable cel to the console
    print(cel)
except:
    # If there is an error in the try block then this string will be displayed in the console
    print('Please enter a number')