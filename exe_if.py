#!/usr/bin/env python
#-*- coding:utf-8 -*-
print '*' * 50


import sys,random

key = random.randint(1,60)
range1 = 10
range2 = 20
range3 = 30
range4 = 40
range5 = 50

if key < range1 or range1 == key :
	print "key = %s <= range1" % key

elif key < range2 or key == range2 :
	print "key = %s <= range2" % key

elif key < range3 or key == range3 :
	print "key = %s <= range3" % key

elif range3 < key <= range4 :
	print "key = %s <= range4" % key

elif key > range4 and key < range5 :
	print "key = %s < range5" % key
elif key >= range5 :
	print "key = %s > range5" % key
