# -------------------------------------------
#	Daily Code	01/09/2021
#   "Functions" Lesson from learnpython.org
#   Coded by: Banehowl
# -------------------------------------------

# Functions are a convenient way to divide your code into useful blocks, allowing order in the code, make it
# more readable, reuse it, and save some time. Also fuctions are a key way to define interfaces so
# programmers can share their code.

# How to write functions in Python
def my_function():                     # Functions are define using the block keyword "def"
    print("Hello From My Function!")

# Functions may also receive arguments (variables passed from the caller to the function)
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))

# Fuctions may return a value to the caller, using the keyword "return"
def sum_two_number(a, b):
    return a + b

# To call functions in Python, simply write teh function's the name followed by (), placing any required
# arguments within the bracket. Using the previous functions we defined:

# print(a simple greeting)
my_function()

# prints - "Hello, Joe Doe, From My Function! I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3
x = sum_two_number(1, 2)
print(x)

