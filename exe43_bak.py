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
		self.scenes = scenes

	def enter(self):
		#The hero will random get a room number
		choice = [i for i in range(1,6)]
		self.luck_number = random.choice(choice)
		print "Your should go to room: %d" % self.luck_number
		return self.luck_number

class Engine(object):
	
	def __init__(self, scene_map):
		pass
	
	def play(self):
		pass
		
class Death(Scene):
	#This Death scene will determine who will win 
	def Whodie(self,):
		death_one = Scene()
		if death_one.pic1 == death_one.enter():
			print "You won, then go to the next scene!"
		else:
			print "You failed, game is over!"

class CentralCorridor(Scene):
	
	def enter(self):
		pass

class LaserWeaponArmory(Scene):

	def enter(self):
		pass

class TheBridge(Scene):

	def enter(self):
		pass

class EscapePod(Scene):

	def enter(self):
		pass

class Map(object):
	
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play() 

		
