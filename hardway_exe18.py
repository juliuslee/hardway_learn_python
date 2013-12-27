#!/usr/bin/env python
#-*- coding:utf-8 -*-
print '*' * 50

# this one like scripts with argv
def print_two(*args):
	arg1, arg2, arg3 = args
	print "arg1: %r, arg2: %r, arg3：%r" % (arg1,arg2,arg3)

#ok, that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

#this just take on argument
def print_one(arg1):
	print "arg1: %r" % arg1

print_two("zed","shaw","third")
print_two_again("zed","shaw")
print_one("First")
