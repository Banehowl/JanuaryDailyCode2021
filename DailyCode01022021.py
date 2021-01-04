# --------------------------------------------------
#	Daily Code	01/02/2021 Variables and Types
# --------------------------------------------------

#you can just assign stuff to variables without saying "var" first
myint = 7
print (myint)

#float is basically a decimal number. you can type out the decimal or make it return as a decimal
myfloat = 7.0
print (myfloat)
myfloat2 = float(7)
print (myfloat2)

#strings (aka str) are defined either with a single quote or double quotes. Double quotes will allow apostrophes '
mystring = 'hello'
print(mystring)
mystring2 = "hello"
print(mystring2)

one = 1
two = 2
three = one + two
print(three)
hello = 'hello'
world = 'world'
helloworld = hello + " " + world
print(helloworld)
#NOTE that you cannot combine numbers and strings (num and str) together in the same variable

#assignments can be done on more than one variable "simultaneously" on the same line
a, b = 3, 4
print(a,b)

#EXERCISE
mystring3 = 'hello'

if mystring3 == hello:
    print("String: %s" % mystring3)