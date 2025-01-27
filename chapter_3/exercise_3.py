# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 1 - Chapter 3 Conditional execution
# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
#
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#
#Example Input and Output
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F

# Display a string to the user. Then have the user input the answer on the same line.
# The input is saved as a string in variable called string_input_score
string_input_score = input('Enter score: ')
# print('You entered a score of:', string_input_score)
try:
    # convert input string value to float value
    float_input_score = float(string_input_score)

    if float_input_score < 0.0 or float_input_score > 1.0:
        raise ValueError('Score must be between 0.0 and 1.0')

    if float_input_score  >= 0.9:
        grade = 'A'
        print(grade)
    elif float_input_score >= 0.8 and float_input_score < 0.9:
        grade = 'B'
        print(grade)
    elif float_input_score >= 0.7 and float_input_score < 0.8:
        grade = 'C'
        print(grade)
    elif float_input_score >= 0.6 and float_input_score < 0.7:
        grade = 'D'
        print(grade)
    elif float_input_score < 0.6:
        grade = 'F'
        print(grade)

except ValueError:
    # If there is an error in the try block then this string will be displayed in the console
    print('Bad score')