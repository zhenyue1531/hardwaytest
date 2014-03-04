from sys import argv
script, filename = argv

print "we're going to erase %r." % filename

raw_input("?")

print "openting the file..."
target = open(filename, 'w')

print "truncating the file,goodbye!"
target.truncate()

print "now i't going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "and finally,we close it."
target.close