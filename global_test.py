#!/usr/bin/env python
#-*- coding:utf-8 -*-
print '*' * 50

global a
a = '132434'

def func0():
	print "I am the zero func"
	print "The a is %s" % a

def func1(one):
	global b 
	b = 'asdff'
	print "Ｉam the one func1 about %s" % one
	print "The b is %s" % b
	print "The a is %s" % a

def func2(two):
	''' hello ,this is a test about the text of function'''
	print "This is the second func2 about %s " % two
	print "The b is %s" % b

func0()
func1('me')
func2('you')
