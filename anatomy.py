# !/usr/bin/python
# Shebang / a hashbang (hashtag and exclamination mark(and it is a file path)
#  Example Python script

# The below line is importing a module that has been hidden - a code in a module container
# it is tapping into our operating system
# Making the code in the sys file (aka module) avaliable to my anatomy.py script
import sys

# argc is a variable and stands for the argument_count - make it more understandable
# len is used to get the number of command line arguments from our hidden module
argument_count = len(sys.argv)
print(argument_count)
if argument_count < 2:
    print("There are less than 2 arguments")
# argv is a part of the sys module

# If the argc is greater than one then it will print 'too many args'
# If the argc is below one then it will go to the else option
if argument_count > 1:
    print("Too many args")
else:
    where = "World"
    # We are passing py2 arguments - a literal value 'the string "Hello"'
    # Hello is the zeroth argument to the print function
    # the where variable the 1st argument to print
    print("Hello", where)
    print("zero", "one", "two")
# This is an example of concatenation
# Concatenation is gluing strings together
# Concatenation uses a + symbol
# string + string
# This is instructing the code to print the string "Goodbye' and the + puts the two together
# The zero is the first place in a sequence
print('Goodbye from' + sys.argv[0])