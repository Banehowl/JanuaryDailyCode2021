# --------------------------------------
#	Daily Code	01/18/2021
#   "Sets" Lesson from learnpython.org
#   Coded by: Banehowl
# --------------------------------------

# Sets are lists with no duplicate entries.

print(set("my name is Eric and Eric is my name".split()))
# This will print out a list containing "my", "name", "is", "Eric",
# and finally "and". Since the rest of the sentence uses words which are already in the set,
# they are not inserted twice.

# Sets are a powerful tool in Python since they have the ability to calculate differences and
# intersections between other sets. For example, let's say you have events A and B:
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

# To find out which members attended both events, you may use the "intersection" method
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

# To find out which members attended only one of the events, use the "symmetric_difference" method
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To find out which members attended only one event and not the other, use the "difference" method
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

# To receive a list of all participants, use the "union" method
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))
