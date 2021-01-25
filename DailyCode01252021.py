# -----------------------------------------------------
#	Daily Code	01/25/2021
#   "Map, Filter, Reduce" Lesson from learnpython.org
#   Coded by: Banehowl
# -----------------------------------------------------

# Map, Filter, and Reduce are paradigms of functional programming. They allow the programmer to write simpler,
# shorter code, without neccessarily needing to bother about intricacies like loops and branching.

# Map

# The map() function in python has the following syntax:

# map(func, *iterables)

# Where func is the function on which each element in iterables (as many as they are) would be applied on.
# Notice the asterisk(*) on iterables? It means there can be as many iterables as possible, in so far func has that
# exact number as required input arguments. Before we move on to an example, it's important that you note the following:

# 1. In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is
# a generator object. To get the result as a list, the built-in list() function can be called on the map object.
# i.e. list(map(func, *iterables))

# 2. The number of arguments to func must be the number of iterables listed.

# Filter

# While map() passes each element in the iterable through a function and returns the result of all elements having
# passed through the function, filter(), first of all, requires the function to return boolean values (true or false)
# and then passes each element in the iterable through the function, "filtering" away those that are false.
# It has the following syntax:

# filter(func, iterable)

# The following points are to be noted regarding filter():

# 1. Unlike map(), only one iterable is required.

# 2. The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed
# to it. Also, as only one iterable is required, it's implicit that func must only take one argument.

# 3. filter passes each element in the iterable through func and returns only the ones that evaluate to true.
# I mean, it's right there in the name -- a "filter".

# Reduce

# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an
# initial argument. It has the following syntax:

# reduce(func, iterable[, initial])

# Where func is the function on which each element in the iterable gets cumulatively applied to, and initial is the
# optional value that gets placed before the elements of the iterable in the calculation, and serves as a default when
# the iterable is empty. The following should be noted about reduce(): 1. func requires two arguments, the first of
# which is the first element in iterable (if initial is not supplied) and the second element in iterable. If initial
# is supplied, then it becomes the first argument to func and the first element in iterable becomes the second element.
# 2. reduce "reduces" (I know, forgive me) iterable into a single value.

