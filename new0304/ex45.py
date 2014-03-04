# -*- coding=utf-8 -*-
from sys import exit
from random import randint
# 战争的游戏，进入战斗后有三次的加血机会，加血过程为猜数过程，猜对加1，猜错减一，血量决定后续进入决斗阶段的猜数次数。战斗后可进入决斗阶段，决斗是乘法算数，算对赢得游戏，算错退出游戏。
class Battle(object):

	def __init__(self, name):
		self.name = name
		
	def main(self):
		print "you can go fighting!!"
		choose = raw_input("are you ready?")
		
		if choose == "yes":
			self.fight()
		else:
			print "you type the wrong word,you should leave."
			exit(1)
			
	def fight(self):
		print "are you ready to fight?"
		lists =["shoot it", "hit it", "beat it", "break it"]
		i = 0
		blood_numbers = 0
		fights = raw_input("how do you want to fight?")

		while i <= 3 and fights in lists[:]:
			
			print "you are lucky, you can enter the next step."
			next_step = raw_input("choose 'enter duel' or 'add blood' room?")
			
			if next_step == "enter duel":
				blood_new = blood_numbers + 2
#				print blood_new
				self.duel(blood_new)
			elif next_step == "add blood":
				blood_number_from = self.blood('0') 
				blood_numbers += blood_number_from
#				print "start", blood_numbers
			else:
				print "please check your room's name."
				continue
			i += 1
		else:
			print "you lost the fighting game."
			self.dead("your answer is wrong")

	def blood(self,number):
		print "you are enter the add blood room"
		data = randint(0, 10)
		self.blood_number = int(number)
		self.blood_number1 = 0
		self.blood_number2 = 0
		
		for i in range(0, 3):
			guess = int(raw_input("guess number"))
			if guess == data:
				self.blood_number1 += 1
				print "you are right"
			else:
				self.blood_number2 += 1
				print "you are wrong"
			
		blood_last = self.blood_number + self.blood_number1 -self.blood_number2
		print blood_last
		return blood_last

	
	def duel(self, blood_num):
		print "you are enter the duel room."
		self.blood = blood_num
		print "you have %d times chance." % self.blood
		mount = [1, 2, 3, 5, 6]
		print mount
		for i in range(0, self.blood):
			enter_infer1 = int(raw_input("you can input the compute number1:"))
			enter_infer2 = int(raw_input("you can input the compute number2:"))
			enter_infer3 = int(raw_input("you can input the answer:"))
			results = mount[enter_infer1 - 1] * mount[enter_infer2 - 1]
			if enter_infer3 == results:
				print "you are won the game!"
				exit(0)
			else:
				print "you are wrong,try again"
				continue
				
		else:
			print "too many times"
			self.dead('you compute wrong')
	
	def dead(self, reason):
		self.reason = reason
		print "%s ,you are dead, see you next time." % reason
		exit(0)
		
try:	
	super_man = Battle("main")
	super_man.main()
except (KeyboardInterrupt, EOFError, ValueError, Exception):
	print "you enter the wrong operate"