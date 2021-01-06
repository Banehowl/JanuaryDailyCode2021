# ---------------------------------------------------------
#	Daily Code	01/06/2021
#   "Basic String Operations" Lesson from learnpython.org
#   Coded by: Banehowl
# ---------------------------------------------------------

aString = "Hello world!"
aString2 = 'Hello world!'

aString3 = "Hello World!"
print("single quotes are ' '")

print(len(aString3))
# len() counts how many characaters in the object. In this case, 12 characters are in Hello World! including
# spaces and punctuation

print(aString3.index("o"))
# This prints 4 because the location of the first occurrence of trhe letter "o" is 4 characters away from the
# first character. There are 2 "o"s in the string however this only gets the first occurrence.
# Remember, Python starts with 0, and not 1, so "o" in "Hello" is at the 4th (5th in normal count) position

print(aString3.count("l"))
# .count will count the number of occurrances. In this case, "l" (lowercase l)

print(aString3[3:7])
# this will slice the string, starting at index 3 and ending at index 6. But why not 7 as indicated? Uh...it's
# easier for most programming languages to do this apparently

print(aString3[3:7:2])
# this prints the characters from  3 to 7, skipping one character. In general form, it's [start:stop:skip]

print(aString3[::-1])
# this will reverse a string

print(aString3.upper())
print(aString3.lower())
# this will CAPS all characters in the string or make them all lowercase

print(aString3.startswith("Hello"))
print(aString3.endswith("asdfasdfasdf"))
print(aString3.endswith("!"))
print(aString3.endswith("World"))
print(aString3.endswith("World!"))
# these will return a True/False response. True that aString3 starts with "Hello". False that it ends with
# "asdfasdfasdf".