# -*- coding: utf-8 -*-
# 定义变量值
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# 将变量输出
print x
print y
# 将变量以字符串形式输出
print "I said: %r." % x
print "I also said: '%s'." % y
# 定义变量
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 输出另一种形式的变量输出
print joke_evaluation % hilarious
# 定义变量
w = "This is the left side of ..."
e = "a string with a right side."
# 输出变量的运算结果
print w + e