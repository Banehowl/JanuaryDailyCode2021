# ----------------------------------------------
#	Daily Code	01/11/2021
#   "Dictionaries" Lesson from learnpython.org
#   Coded by: Banehowl
# ----------------------------------------------

# Dictionary is a data type similar to arrays, but works with keys and values instead of indexes
# Each calue stored in a dictionary can be accessed using a key, which is any type of object (a string,
# a number, a list, etc.) instead of using its index to address it.

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# This can also be written as

phonebook2 = {
    "Jacob"  : 938477567,
    "Jingle" : 938377265,
    "Himer"  : 947662782
}
print(phonebook2)

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. However a diction, unlike a list, does not keep the
# order of the values stored in it.

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a specified index, use either one of these notations
del phonebook["John"]
print phonebook

phonebook2.pop("Jacob")
print(phonebook2)