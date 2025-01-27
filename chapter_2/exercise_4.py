# CIT-95-21257-2024SP: Python Programming
# Miguel Quezada
# Module 1 - Chapter 2
# Exercise 4: Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
#
# For each of the following expressions, write the value of the expression and the
# type (of the value of the expression).
#
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5

# Assigns the integer value 17 to the variable called width
width = 17
# Assigns the float value 12.0 to the variable called height
height = 12.0

# Example 1 - Performs integer division on two integers
# The // operator performs floor division.
# In floor division after the division of two integers, the result is rounded down to the nearest integer
# The result is displayed in the console.
print(width//2)
# The type function returns the data type of a value.
# Displays the data type of the result of the division.
print(type(width//2))

# Example 2 - Performs division on two float numbers
# Dividing by a float ensures the result is also a float
# The result is displayed in the console.
print(width/2.0)
# Displays the data type of the result of the division.
print(type(width/2.0))

# Example 3 - Performs division on a floating-point number by an integer. The result is an integer
# The result is displayed in the console.
print(height/3)
# Displays the data type of the result of the division.
print(type(height/3))

# Example 4 - Uses order of precedence to perform a calculation.
# The order of precedence is parentheses, exponents, multiplication, division, addition, subtraction
# The result is displayed in the console.
print(1 + 2 * 5)
# Displays the data type of the result of the division.
print(type(1 + 2 * 5))