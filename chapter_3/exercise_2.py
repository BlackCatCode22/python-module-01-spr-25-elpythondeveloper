# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 1 - Chapter 3 Conditional execution
# Exercise 2: Rewrite your pay program using try and except so that your
#             program handles non-numeric input gracefully by printing a message
#             and exiting the program.
#The following shows two executions of the program:
#
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
#
# Enter Hours: forty
# Error, please enter numeric input

try:
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

    # check if employee worked more than 40 hours
    if float_input_hours > 40:
        regular_hours = 40
        # Get the number of hours above 40
        overtime_hours = float_input_hours - 40
    else:
        overtime_hours = 0
        regular_hours = float_input_hours

    float_regular_pay = regular_hours * float_input_rate
    overtime_rate = float_input_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate
    total_pay = float_regular_pay + overtime_pay
    # ----- Section 2 - Perform Calculation -----

    # ----- Section 3 - Display Output -----
    # Display the string Pay: followed by the value stored in variable total_pay in the console
    print("Pay:", total_pay)
    # ----- Section 3 - Display Output -----

except:
    # If there is an error in the try block then this string will be displayed in the console
    print('Error, please enter numeric input')