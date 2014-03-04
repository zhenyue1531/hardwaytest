# -*- coding=utf-8 -*-
from sys import exit
from random import randint

class Game(object):
	def __init__(self, start):
		self.quips = [
			"you died"
		]
		self.start = start
	
	def play(self):
		next_room_name = self.start
		
		while True:
			print "\n---"
			print next_room_name
			room = getattr(self, next_room_name)   # 
			next_room_name = room()                # 调用方法room()，将返回值付给next_room_name.


			
	def death(self):
		print self.quips[randint(0, len(self.quips) - 1)]
		exit(1)
		
	def central_corridor(self):
		print "you are in central_corridor"
		
		action = raw_input(">")
		
		if action == "shoot!":
			print "shoot,so died"
			return 'death'
		elif action == "tell a joke":
			print "enter laser room"
			return 'laser_weapon_armory'
		else:
			print "continue center"
			return 'central_corridor'

	def laser_weapon_armory(self):
		print "you will enter the last room"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("guess")
		guesses = 0
	
		while guess != code and guesses < 10:
			print "wrong"
			guesses += 1
			guess = raw_input("guess")
		
		if guess == code:
			print "you are won!"
			exit(0)
		else:
			print "wrong"
			return 'death'
		
games = Game("central_corridor")
games.play()