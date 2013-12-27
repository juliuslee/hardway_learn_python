#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Animal(object):
	print "hi"

class Dog(Animal):
	print "this is from Dog(Animal)"
	def __init__(self,name):
		self.name = name

class Cat(Animal):
	print "this is from Cat(Animal)"
	def __init__(self,name2):
		self.name = name2
		
