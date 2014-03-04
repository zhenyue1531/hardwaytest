# create a mapping of state to abbreviation
states = {
	'oregon': 'or',
	'florida': 'fl',
	'california': 'ca',
	'michigan': 'mi'
}

# create a basic set of states and some cities in them
cities = {
	'ca': 'san francisco',
	'mi': 'detroit',
	'fl': 'jacksonville'
}

# add some more cities
cities['ny'] = 'new york'
cities['or'] = 'portland'

# print out some cities
print "_" * 10
print "ny state has:", cities['ny']
print "or state has:", cities['or']

# print some states
print "_" * 10
print "m is :", states['michigan']
print "f is:", states['florida']

# do it by using the state then cities dict
print '_' * 10
print "m has:", cities[states['michigan']]
print "f has:", cities[states['florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '_' * 10
# safely get a abbreviation by state the might not be there
state = states.get('texas', None)

if not state:
	print "sorry, no texas."
	
# get a city with a default value
city = cities.get('tx', 'Does not exist!')
print "the city for the state 'tx' is : %s" % city