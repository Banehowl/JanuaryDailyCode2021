# ----------------------------------------------------
#	Daily Code	01/18/2021
#   "Exception Handling" Lesson from learnpython.org
#   Coded by: Banehowl
# ----------------------------------------------------

# Python's solution to errors are exceptions. For example

# print(a)

# #error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# </module></stdin>

# The error above happens when we forget to define a. However, it can be bypass like so:

def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()