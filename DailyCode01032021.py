# --------------------------------
#	Daily Code	01/03/2021 List
# --------------------------------

#List are very similar to arrays. Below is a simple list
myList = []
myList.append(1)
myList.append(2)
myList.append(3)
print(myList[0]) #prints 1
print(myList[1]) #prints 2
print(myList[2]) #prints 3

#prints out 1, 2, 3
for x in myList:
    print(x)

myList2 = [1,2,3,4,5]
print(myList2[4])

#Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)