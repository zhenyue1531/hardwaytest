
from sys import argv

script, user_name, age = argv
prompt = '--'

print "hi %s, i'm the %s script." % (user_name,script)
print "i'd like to ask you a few questions."
print "do you like me %s?" % user_name
print "%s years old is too old for you." % age
likes = raw_input(prompt)

print "where do you live %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print '''
alright, so you said %r about liking me.
you live in %r. not sure where what is.
and you have a %r computer.nice
''' % (likes, lives, computer)