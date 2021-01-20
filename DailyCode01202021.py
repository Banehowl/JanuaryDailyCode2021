# -----------------------------------------------
#	Daily Code	01/20/2021
#   "Serialization" Lesson from learnpython.org
#   Coded by: Banehowl
# -----------------------------------------------

# Python provides built-in JSON libraries to encode and decode JSON
# Python 2.5, the simplejson module is used, whereas in Python 2.7, the json module is used.

# In order to use the json module, it must be imported:
import json

# There are two basic formats for JSON data. Either in a string or the object datastructure.
# The object datastructure, in Python, consists of lists and dictionaries nested inside each other.
# The object datastructure allows one to use python methods (for lists and dictionaries) to add, list,
# search and remove elements from the datastructure.
#
# The String format is mainly used to pass the data into another program or load into a datastructure.

# To load JSON back to a data structure, use the "loads" method. This method takes a string and turns
# it back into the json object datastructure. To encode a data structure to JSON, use the "dumps" method.
# This method takes an object and returns a String:

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json.loads(json_string))

# Sample Code using JSON:
# import json #it's already imported so...

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])