# ---------------------------------------------------------
#	Daily Code	01/28/2021
#   "Convert Minutes into Seconds" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------

# Write a function that takes an integer minutes and converts it to seconds
# convert(5) -> 300
# convert(3) -> 180
# convert(2) -> 120

def convert(minutes):
    seconds = minutes * 60
    return(seconds)

print convert(5)
print convert(3)
print convert(2)