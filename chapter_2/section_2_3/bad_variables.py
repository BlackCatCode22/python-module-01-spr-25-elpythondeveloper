# ----- Python Variable Rules -----
# Reference
# https://peps.python.org/pep-0008/#package-and-module-names
# A variable name must begin with a letter or underscore.
# A variable name can’t contain spaces, punctuation, or special characters other than the underscore.
# A variable name can’t begin with a number, but can use numbers later in the name.
# A variable name can’t be the same as a keyword that’s reserved by Python.
# ----- Python Variable Rules -----
# ----- Examples of declaring variables -----
# x = 10      # x is an integer (int)
# y = 3.14   # y is a floating-point number (float)
# name = "Alice"  # name is a string (str)
# In Python, you can use either single quotes or double quotes for strings
# ----- Examples of declaring variables -----

# Examples of bad variable names - since these wont run I commented them out
# # this is incorrect because a variable cant begin with numbers
# 76trombones = 'big parade'
# # this is incorrect because a variable cant contain special characters lik @
# more@ = 1000000
# # this is incorrect because class is a Python keyword and variable cant use a keyword
# class = 'Advanced Theoretical Zymurgy'

# Examples of correct way to write the variables
seventy_six_trombones = 'big parade'
more_at = 1000000
string_called_class = 'Advanced Theoretical Zymurgy'

# display the value stored in the variable called seventy_six_trombones in the console
print(seventy_six_trombones)
# display the value stored in the variable called more_at in the console
print(more_at)
# display the value stored in the variable called string_called_class in the console
print(string_called_class)