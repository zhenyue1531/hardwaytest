# -*- coding:utf-8 -*-
def break_words(stuff):
	'''this function will break up words for us.'''
	words = stuff.split(' ')  #��ÿ�����ʷָ�м����ո�
	return words
	
def sort_words(words):
	'''sorts the words.'''
	return sorted(words)      #�Ե��ʽ�������
	
def print_first_word(words):
	'''print the first word after popping it off.'''
	word = words.pop(0)       #��õ�һ��Ԫ��
	print word
	
def print_last_word(words):
	'''print the last word after popping it off.'''
	word = words.pop(-1)     #������һ��Ԫ��
	print word
	
def sort_sentence(sentence):
	'''take in a full sentence and returns the sorted words.'''
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	'''print the first and last words of the sentence'''
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	'''sorts the words then prints the first and last one.'''
	break_sentence = break_words(sentence)
	print break_sentence
	words = sort_words(break_sentence)
	print words
	print_first_word(words)
	print_last_word(words)
	
show = raw_input("insert a sentence:")
print show
print_first_and_last_sorted(show)