#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random

class Scene(object):
	#define diff scene's pictures
	pic1 = 1
	pic2 = 2
	pic3 = 3
	pic4 = 4
	pic5 = 5

	def __init__(self,scenes):
		self.scene = scenes
		print "I am the Scene of object.", self.scene

	def enter(self):
		#The hero will random get a room number
		choice = [i for i in range(1,6)]
		self.luck_number = random.choice(choice)
		print "Your should go to room: ", self.luck_number
		return self.luck_number

class Death(Scene):
	#This Death scene will determine who will win 
	def Whodie(self):
		death_one = Scene()
		if death_one.pic1 == death_one.enter():
			print "You won, then go to the next scene!"
		else:
			print "You failed, game is over!"

class CentralCorridor(Scene):
	
	def enter(self):
		pass

def main():
	Death('hi')


main()
