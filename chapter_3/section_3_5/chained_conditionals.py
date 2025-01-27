# Chapter 3 - Conditional execution
# 3.5 Chained conditionals
# Sometimes there are more than two possibilities. In such cases, we need more than two
# branches. One way to express a computation like that is a chained conditional

# -----------------------------------------------------------------------------------------
# Example 1 - Alternative execution if statement using less than and greater than operators
# Save the integer value 9 in a variable called x
x = 9
# Save the integer value 4 in a variable called y
y = 4

# if the value stored in variable x is less than the value stored in variable y
# then this condition returns True otherwise this condition returns False
if x < y:
    # If the condition returns True then this string will be displayed in the console
    print('x is less than y')
# if the value stored in variable x is greater than the value stored in variable y
# then this condition returns True otherwise this condition returns False
elif x > y:
    # If the condition returns True then this string will be displayed in the console
    print('x is greater than y')
# for any other condition such as when the value in x equals the value in y
# then this condition would be executed
else:
    print('x and y are equal')
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# Example 2 - Alternative execution if statement using equality == operator
# Save the string value b in a variable called choice
choice = 'b'

# if the value stored in variable choice equals a then this condition returns True
# otherwise this condition returns False
if choice == 'a':
    # If the condition returns True then this string will be displayed in the console
    print('Bad guess')
# if the value stored in variable choice equals b then this condition returns True
# otherwise this condition returns False
elif choice == 'b':
    # If the condition returns True then this string will be displayed in the console
    print('Good guess')
# if the value stored in variable choice equals c then this condition returns True
# otherwise this condition returns False
elif choice == 'c':
    # If the condition returns True then this string will be displayed in the console
    print('Close, but not correct')
# -----------------------------------------------------------------------------------------