# mylist = []

# mylist.append(1)
# mylist.append(2)
# print(mylist)

# for x in mylist:
#     print(x)

# # accesing an index which does not exist
# # #generates an exception/error

# mylist = [1,2,3]
# #print(mylist[10])

# numbers = []
# strings = []
# names = ['John', 'James', 'Kat']

# names.append('Mason')
# print(names)
# print(names[3])

# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(4)
# del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
for num in x:
    print(num * 1000)
