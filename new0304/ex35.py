from sys import exit

def gold_room():
	print "this room is full of gold. how much do you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
#	if int(next) is True:
		how_much = int(next)
	else:
		dead("man,learn to type a number.")
		
	if how_much < 50:
		print "nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("you greedy bastard!")
		
def bear_room():
	print "there is a bear here."
	bear_moved = False
	
	while True:
		next = raw_input(">")
		
		if next == "take honey":
			dead("the bear slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "the bear has moved from the door."
			bear_moved = True
		elif next =="taunt bear" and bear_moved:
			dead("the bear chews your leg off.")
		elif next =="open door" and bear_moved:
			gold_room()
		else:
			print "i got no idea what that means."

def cthulhu_room():
	print "here you see the great evil cthulhu."
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty!")
	else:
		cthulhu_room()
		
def dead(why):
	print why, "good job!"
	exit(0)

def start():
	print "you are in a dark room."
	
	next = raw_input(">")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")
		
start()