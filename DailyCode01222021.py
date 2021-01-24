# --------------------------------------------
#	Daily Code	01/22/2021
#   "Decorators" Lesson from learnpython.org
#   Coded by: Banehowl
# --------------------------------------------

# Decorators allow you to make simple modifications to callable objects like functions,
# methods, or classes. We shall deal with functions for this tutorial. The syntax

def function(arg):
    return "value"
function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions

# As you may have seen, a decorator is just another function which takes a functions and returns one.
# For example you could do this:

def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args
                                     # and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value