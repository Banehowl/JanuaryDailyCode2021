# --------------------------------------------------
#	Daily Code	01/04/2021
#   "String Formatting" Lesson from learnpython.org
#   Coded by: Banehowl
# --------------------------------------------------

# Here are some basic agrument specifiers you should know:
# %s                    - String (or any object with a  string representation, like numbers)
# %d                    - Integers
# %f                    - Floating point numbers (like decimals)
# %.<number of digits>f - Floating point numbers with a fixed amount of digits
#                         to the right of the dot (think rounding)
# %x%X                  - Integers in hex representation (lowercase/uppercase)

# This prints out "Hello, John!"
name = "John"
print("Hello %s!" % name)

#To use two or more agument specifiers, use a tuple (parentheses)

# This prints out "John is 23 years old"
name1 = "Bob"
age1 = 23
print("%s is %d years old" % (name1, age1))

# Any object which is not a string can be formatted using the %s operator as well
# The string which returns from the "repr" method of that object is formatted as the string

# This prints out: A list: [1, 2, 3]
myList = [1, 2, 3]
print("A list %s" % myList)

# Exercise
data = ("John", "Doe", 54.44)
format_string = "Hello %s %s. Your current balance is $%s"

print(format_string % data)
# So it will just put it out in order of %s called. Moving it around it can become "Hello Doe 54.44
# Your current balance is $John" if the data tuple is ordered in that way ("Doe, 54.44, John).