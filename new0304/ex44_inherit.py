class Parent(object):
	
	def implicit(self):
		print "parent implicit()"
		
	def altered(self):
		print "parent override()"
		
class Child(Parent):
	
	def altered(self):
		print "child, before parent altered()"
		super(Child, self).altered()
		print "child, after parent"
		
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
dad.altered()
son.altered()