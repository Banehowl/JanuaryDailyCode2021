# --------------------------------------------
#	Daily Code	01/07/2021
#   "Conditions" Lesson from learnpython.org
#   Coded by: Banehowl
# --------------------------------------------

# Python uses boolean logic to evaluate conditions aka True/False
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3)  # prints out True
print(x != 3) # prints out True / != means not equals

# Boolean operators "and" and "or". So it'll seek out both or either conditions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

# "in" operator could be used to check if a specified object exist within a iterable object like a list
name1 = "Joe"
if name1 in ["Joe", "Rick"]:
    print("Your name is either Joe or Rick")

x1 = 2
if x1 == 2:
    print("x equals two!")
else:
    print("x does not equal 2")

# "is" operator is not like the "==" operator as it does not match the values, but the instances themselves
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x3 == y3) # prints out true
print(x3 is y3) # prints out false

# "not" before a boolean expression inverts it
print(not False) #prints out true
print(not True)  #prints out false
print((not False) == (False)) #prints out false