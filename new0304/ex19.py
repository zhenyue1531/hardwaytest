def a_and_b(a_count, b_count):
	print "you have %d a!" % a_count
	print "you have %d b!" % b_count
	
print "we can give the numbers!"
a_and_b(20, 30)

print "or ,we can use from our script:"
amount_a = 10
amount_b = 50
a_and_b(amount_a, amount_b)

print "we can even do math"
a_and_b(10+20, 5+6)

print "we can combine the two"
a_and_b(amount_a + 100,amount_b + 1000)