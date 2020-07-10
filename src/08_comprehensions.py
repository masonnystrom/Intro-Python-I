"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for num in range(5):
    y.append(num)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y2 = []
for num in range(0,9):
    y2.append(num **2)
print(y2)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
y3 = []
a = ["foo", "bar", "baz"]

for string in a:
    y3.append(string.upper())

print(y3)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
x_even = []
x = input("Enter comma-separated numbers: ").split(',')
print(x)

for num in x:
    num = int(num)
    if num % 2 == 0:
        x_even.append(num)
print(x_even)