#!/usr/bin/env python
#-*- coding:utf-8 -*-
print '*' * 50

def cheese_and_crackers(cheese_count,boxes_of_crackers): #Give the function two values
	print "You have %d cheeses!" % cheese_count #Pass the first value
	print "You have %d boxes of crackers!" % boxes_of_crackers  #Pass the second value
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two,variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def count(a, b):
	c = a + b
	return c
def crackers(e, f):
	g = e + f
	return g

print "Here use the function to pass the arguments"
cheese_and_crackers(count(3, 5),crackers(8, 9))
