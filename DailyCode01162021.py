# -------------------------------------------------------------
#	Daily Code	01/16/2021
#   "Multiple Function Arguments" Lesson from learnpython.org
#   Coded by: Banehowl
# -------------------------------------------------------------

# Every function is Python receives a predefined number of arguments, if declared normally like this:
# def myFunction(first, second, third)

# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

# In this example, 'therest' variable is a list of variables, which receives all arguments which were
# given to the 'foo' function after the first 3 arguments.

# So calling foo(1,2,3,4,5) will print out:
foo(1,2,3,4,5)

# It is also possible to send functions arguments by keyword, so that the order of the argument
# does not matter, using the following syntax:

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" % (result))