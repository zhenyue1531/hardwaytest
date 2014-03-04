the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']

for number in the_count:
	print "this is count %d" % number
	
for fruit in fruits:
	print "a fruit of type: %s" % fruit
	
elements = []

for i in range(0,6):
	print "adding %d into elements" % i
	elements.append(i)
	
for i in elements:
	print "element is %d" % i