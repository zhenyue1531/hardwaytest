# -*- coding:uft-8 -*-
from sys import argv, exit
scritp, choose = argv


def measure():
	print "you will enter a guess number's game."
	data = 25
	
	for i in range(0, 5):       # for ���Ǹ���i in ����
		measure = int(raw_input("you should guess the number:"))
		
		if measure > data:
			print "too large,try smaller."
		elif measure < data:
			print "too small ,try larger."
		else:
			print "you are right."
			break               # ����¶��ˣ�ֱ���˳�����ѭ����               
			
	else:
		measure = int(raw_input("you should guess the number?"))
		dead("you try too many times")
		
def dead(reason):
	print "%s,you are dead!" % reason
	exit(0)
	
def count():
	number_list = [2, 4, 6, 8, 10, 12]
	print "the number list is:", number_list
	count1 = int(raw_input("you should input the compute number1:"))
	count2 = int(raw_input("you should input the compute number2:"))
	result = number_list[count1 - 1] * number_list[count2 - 1]        #���������б�һ������-1����
	answer = int(raw_input("you should input the answer:"))
	if result == answer:
		print "you are clever!"
	else:
		print "you are wrong!"
# ѡ��measure���������ִ�С����Ϸ��ѡ��count��������б�˻�����Ϸ��		
if choose == "measure":
	measure()
elif choose == "count":
	count()
else:
	dead("your begin is over")
