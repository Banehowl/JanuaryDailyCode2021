# -----------------------------------------------
#	Daily Code	01/29/2021
#   "Area of a Triangle" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Write a function that takes the base and height of a triangle and return its area

# tri_area(3 , 2) -> 3
# tri_area(7, 4) -> 14
# tri_area(10, 10) -> 50

def tri_area(base, height):
    area = base * height / 2
    return(area)

print tri_area(3 , 2)
print tri_area(7, 4)
print tri_area(10, 10)