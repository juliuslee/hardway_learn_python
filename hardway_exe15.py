#!/usr/bin/env python
#-*- coding:utf-8 -*-
print '*' * 50

from sys import argv
script, filename = argv

text = open(filename)
print "Here is your file %r:" % filename
print text.read()
text.close()
#print "Type the filename again:"
#file_again = raw_input(">>>")

#txt_again = open(file_again)
#print txt_again.read()
