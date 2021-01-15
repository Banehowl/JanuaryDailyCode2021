# -----------------------------------------------------
#	Daily Code	01/12/2021
#   "List Comprehensions" Lesson from learnpython.org
#   Coded by: Banehowl
# -----------------------------------------------------

# List comprehensions is a very powerful tool, which creates a new list based on another list
# in a single, readable line.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split() #'.split" is the key
word_lengths = [] #creates a empty array/list
for word in words:
    if word != "the": # remember that this is case senstive, so "The" and "the" are different
        word_lengths.append(len(word))
print(words)
print(word_lengths)

# This can be simplified to this
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)
