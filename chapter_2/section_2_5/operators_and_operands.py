# Operators are special symbols that represent computations like addition and multiplication.
# The values the operator is applied to are called operands.
# operators +, -, *, /, and ** perform addition, subtraction, multiplication, division, and exponentiation

# example 1 - add two integers and display the result in the console
print('The sum of 20 and 32 is:', 20 + 32)

# example 2 - subtract 1 from the value stored in variable hour and display the result in the console
hour = 8
print (hour-1)

# example 3 - multiply the value stored in variable hour by 60
# and then add the value stored in variable minute and display the result in the console
minute = 5
print (hour*60+minute)

# example 4 - divide the value stored in variable minute by 60 and display the result in the console
# In Python 3.x, the result of this division is a floating point result
print (minute/60)

# example 5 - find 5 to the 2nd power and display the result in the console - result should be 25
print (5**2)

# example 6 - use order of operation and display the result in the console - result should be 112
# The operations inside parentheses are calculated first
# 5 is added with 9 first which is 14, then 15 is subtracted by 7 which is 8. Then 14 is multiplied by 8.
print ( (5+9)*(15-7) )