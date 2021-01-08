# ---------------------------------------
#	Daily Code	01/08/2021
#   "Loops" Lesson from learnpython.org
#   Coded by: Banehowl
# ---------------------------------------

# There are two loops in Python, "for" and "while"
# "For" loops iterate over a give sequence
primes = [2, 3, 5, 7]
for prime in primes: # note here that prime was no defined until now and still works, even in the loop
    print(prime)

# "For loops can iterate over a sequence of numbers using the "rage" and "xrange" functions.
# Difference between "range" and "xrange" is that the range function returns a new list with numbers
# of that specified range, whereas xrange returns an interator, which is more efficient

# Prints out the number 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# Prints out 3, 4, 5
for x in range(3, 6): # note that the range function works like this range(start, stop, step)
    print(x)

# Prints out 3, 5, 7
for x in range(3, 8, 2):
    print(x)

# "While" loops repeat as long as a certain boolean condition is met
# Prints out 0, 1, 2, 3, 4
count = 0
while count < 5:
    print(count)
    count += 1 # this is the same as count = count + 1

# "break" is used to exit a for loop or a while loop, whereas continue is used to skip the current block
# and return to the "for" or "while" statement.
# Prints out 0, 1, 2, 3, 4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers 1, 3, 5, 7, 9
for x in range(10):
    # Checks if x is even
    if x % 2 == 0: # "if x divided by 2 has a remainder of 0"
        continue
    print(x) # this decrease in indent means else without typing it

# Unlike langauges like C, CPP.. we can use else for loops. When the loop condition for "for" or "while"
# statement fails then code part in "else" is executed. If a break statement is executed inside the
# for loop then the "else" part is skipped. Note that the "else part is executed even if there is a continue
# statement.

# Prints out 0, 1, 2, 3, 4 then it prints "count value reached 5"
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

# Prints out 1, 2, 3, 4
for i in range(1, 10):
    if (i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


