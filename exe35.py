#/bin/env python
#-*- encoding:UTF-8 -*-

from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(">>")
	if "0" in next or "1" in next :   #判断输入是否符合，类似于case
		how_much = int (next)     #进行类型转换
	else :
		dead("Man , learn to type a number .")
	
	if how_much < 50:                 #判断大小
		print "Nice, you are not greedy ,you win !"
		exit(0)                      #退出程序
	else :
		dead ("You greedy bastard !")

def bear_room():
	print '''
There is a bear here .
The bear  has a bunch of honey .
The fat bear is in front of another door .
How are you going to move the bear? 
'''
	bear_moved = False                   #定义初始值为false

	while True :                         #无限循环
		next = raw_input(">>")

		if next == "take honey":
			dead ('The bear looks at you then slaps your face off .')
		elif next == 'taunt bear' and not bear_moved :
			print "The bear has moved from the door .you can go through it now ." 
			bear_moved = True    #这一步以后才被赋值为真
		elif next == 'taunt bear' and bear_moved :
			dead ("The bear gets pissed off and chews your leg off .")
		elif next == 'open door' and bear_moved:    #这种条件下才能进入gold_room
			gold_room()
		else :
			print "I got no idea what that means ."

def cthulhu_room():
	print '''
Here you see the great evil cthulhu .
He ,it ,whatever stares at you and you go insane .
Do you flee for your life or eat your head ?
'''

	next = raw_input(">>")

	if "flee" in next :    #如果为真则重新开始
		start ()
	elif "head" in next :
		dead ('well that was tasty !')
	else :
		cthulhu_room()  #都没有输入正确，则再重新开始

def dead (why):
	print why ,"Good job !" #两个字符串连在一起的写法
	exit(0)

def start ():
	print '''
You are in a dark room .
There is a door to your right and left .
Which one do you take ?
'''
	next = raw_input(">>")

	if next == 'left':
		bear_room()
	elif next == 'right':
		cthulhu_room()
	else :
		dead ("You stumble around the room until you starve .")

start()

