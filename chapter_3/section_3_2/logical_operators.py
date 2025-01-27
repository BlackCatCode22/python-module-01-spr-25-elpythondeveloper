# Chapter 3 - Conditional execution
# 3.2 Logical operators
# There are three logical operators: and, or, and not

# Example 1 - Using and operator where value returns True
# Save the integer value 9 in a variable called x
x = 9
# For the and operator to return True, both expressions have to be true.
# In this case since x is greater than 0 and x is less than 10, this expression should return True
print(x > 0 and x < 10)

# Example 2 - Using and operator where value returns False
# Save the integer value 9 in a variable called x
x = 14
# For the and operator to return True, both expressions have to be true.
# In this case x is greater than 0 but x is not less than 10, so this expression should return False
print(x > 0 and x < 10)