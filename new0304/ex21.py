def add(a, b):
	print "adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "subtracting %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "multiplying %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "diving %d / %d" % (a, b)
	return a / b
	
print "let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

#a puzzle for the extra credit, type it in anyway.
print "here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that decomes:", what, "can you do it by hand?"

other = add(age, subtract(multiply(divide(weight, 2), iq), height))
print "other is %r" % other