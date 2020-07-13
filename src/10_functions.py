import random
# Write a function is_even that will return true if the passed-in number is even.
def mult2(x):
    return x * 2
print(mult2)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def iseven(num):
    if num % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(iseven(num))

