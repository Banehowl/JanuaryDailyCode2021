# -----------------------------------------------------
#	Daily Code	01/10/2021
#   "Classes and Objects" Lesson from learnpython.org
#   Coded by: Banehowl
# -----------------------------------------------------

# Objects are an encapsulation of variables and functions into a sign entity. Objects get their variables and
# functions from classes

class myClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myObjectx = myClass() # now the variable "myObjectx" holds an object of class "myClass" that contains the
                      # variable and the function defined within the class called "myClass"

# Accessing Object Variables. This will print out the string 'blah'
print(myObjectx.variable) # "variable" is defined insid ethe class and can be called out with "."

# You can create multiple objects that are of the same class(have the same variables and functions defined)
# However, each object contains independent copies of the variables defined in teh class. For example:

myObjecty = myClass()
myObjecty.variable = "yackity"

print(myObjecty.variable)

# To access a function inside of a object you use notation similar to accessing variable:
myObjectx.function()

