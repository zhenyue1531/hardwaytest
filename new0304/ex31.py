print "you enter a room"

door = raw_input(">")

if door == "1":
	print "insert bear"
	
	bear = raw_input(">")
	
	if bear == "1":
		print "bear=1"
	elif bear == "2":
		print "bear=2"
	else:
		print "bear is %s" % bear
		
elif door == "2":
	print "insert insanity"
	
	insanity = raw_input(">")
	
	if insanity == "1" or insanity == "2":
		print "insanity is small"
	else:
		print "insanity is %s" % insanity

else:
	print "door is out"