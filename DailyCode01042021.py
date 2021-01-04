# --------------------------------------------------
#	Daily Code	01/04/2021
#   "Basic Operations" Lesson from learnpython.org
#   Coded by: Banehowl
# --------------------------------------------------

#Arithmetic Operators - basically addition, subtraction, multiplication, and division works. PEMDAS applies
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)
# 11 / 3 = 3 if printed however 11 % 3 will give the remainder of 2

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
# the "**" raises the number to the power of whatever number after it

#Operators with strings aka using operations like "+" to add works into sentences
helloworld = "hello" + " " + "world"
print(helloworld)

#You can also multiply strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

#Operators with List
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
#so this won't add the numbers together, rather, add them to the List, appended to the end in this case

print([1,2,3]*3)
#this will simply repeat the list 3 times, not multiply the List numbers by 3