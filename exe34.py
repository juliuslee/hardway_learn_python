#!/bin/env python
#-*- coding:utf-8 -*-

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
t = ['first' ,'second' ,'third' ,'fourth' ,'fifth' ,'sixth' ]


for i in range(0,6):
	print "The %r animal is at %d and is a %r ." %( t[i], i, animals[i])
	print "The animal at %d is the %r and is a %r ." %( i, t[i], animals[i])
