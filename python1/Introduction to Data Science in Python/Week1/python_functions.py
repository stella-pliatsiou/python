# This function should add the two values if the value of the "kind" parameter is "add" 
# or is not passed in, otherwise it should subtract the second value from the first. 

# Can you fix the function so that it works?

# def do_math(?, ?, ?):
#   if (kind=='add'):
#     return a+b
#   else:
#     return a-b

# do_math(1, 2)


def do_math(a, b, kind='add'):
    if (kind=='add'):
        return a+b
    else:
        return a-b

do_math(1, 2)

#-------------------------------------------------------------------------------------
# Question 2
# Here's our first bit of interaction, why don't you try and change this function to 
# accept three parameters instead of two and return the sum of all three.

def add_numbers(x, y, z):
    return x+y+z

print(add_numbers(1, 2, 3))