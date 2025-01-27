# Chapter 3 - Conditional execution
# 3.6 Nested conditionals
# A conditional statement like an if statement can be nested within another.


# Example 1 - Nested conditional
# Instead of writing an if statement with 3 conditions we can write a nested conditional if statement
# Save the integer value 9 in a variable called x
x = 9
# Save the integer value 4 in a variable called y
y = 4

# if the value stored in variable x equals the value stored in variable y
# then this condition returns True otherwise this condition returns False
if x == y:
    # If the condition returns True then this string will be displayed in the console
    print('x and y are equal')
else:
    # if the value stored in variable x is greater than the value stored in variable y
    # then this condition returns True otherwise this condition returns False
    if x < y:
        # If the condition returns True then this string will be displayed in the console
        print('x is less than y')
    else:
        # If the condition returns False then this string will be displayed in the console
        print('x is greater than y')


# -----------------------------------------------------------------------------------------
# # Example 1 - Alternative execution if statement with 3 conditions
# # Save the integer value 9 in a variable called x
# x = 9
# # Save the integer value 4 in a variable called y
# y = 4
#
# # if the value stored in variable x is less than the value stored in variable y
# # then this condition returns True otherwise this condition returns False
# if x < y:
#     # If the condition returns True then this string will be displayed in the console
#     print('x is less than y')
# # if the value stored in variable x is greater than the value stored in variable y
# # then this condition returns True otherwise this condition returns False
# elif x > y:
#     # If the condition returns True then this string will be displayed in the console
#     print('x is greater than y')
# # for any other condition such as when the value in x equals the value in y
# # then this condition would be executed
# else:
#     print('x and y are equal')
# -----------------------------------------------------------------------------------------

