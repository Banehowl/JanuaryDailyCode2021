# ---------------------------------------------------
#	Daily Code	01/21/2021
#   "Partial Functions" Lesson from learnpython.org
#   Coded by: Banehowl
# ---------------------------------------------------

# You can create partial functions in python by using the partial function from the functools library
# Partial functions allow one to derive a function with x parameters to a function with fewer parameters
# and fixed values set for the more limited function.

from functools import partial # functools is standard import library

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2) # dbl is imported from functools
print(dbl(4))

# Sample Code
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))
