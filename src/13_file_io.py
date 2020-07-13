"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('src/foo.txt', 'r')
print(f.read())
f.close()

with open('src/foo.txt') as f:
    read_data = f.read()
print(read_data)
f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open('bar.txt', 'w')
bar.write(""" if you can keep you're head about you while all about you are losing theirs and blaming it on you,
if you can trust yourself when all men doubt you.""")
bar.close()
