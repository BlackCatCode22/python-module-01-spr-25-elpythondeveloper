# Chapter 3 - Conditional execution
# 3.4 Alternative execution
# A second form of the if statement is alternative execution,
# in which there are two possibilities and the condition determines which one gets executed.

# Example 1 - Alternative execution if statement

# Save the integer value 9 in a variable called x
x = 8

# if the value stored in variable x divided by 2 returns a remainder 0 then the condition returns True
if x%2 == 0 :
    # If the condition returns True then this string will be displayed in the console
    print('x is even')
else :
    # If the condition returns False then this string will be displayed in the console
    print('x is odd')