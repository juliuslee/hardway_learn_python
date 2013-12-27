#!/bin/env python
#-*- coding: utf-8 -*-

def while_exe(stop):

	i = 0
	numbers = []

	while i < stop :
		print "At the top i is %d " % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now : ", numbers
		print "At the bottom i is %d " % i 

	print "The numbers :"

	for num in numbers:
		print num 

while_exe(9)
