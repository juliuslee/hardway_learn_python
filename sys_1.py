#!/bin/env python
#-*-coding: utf-8-*-

import os,commands,re,string

def Mem(key):
	mem = re.compile('Mem:.*').search(key).group()
	print mem

def Cpu(key):
	cpu = re.compile('Cpu.*').search(key).group()
	print cpu

def Task(key):
	task = re.compile('Task.*').search(key).group()
	print task

def Swap(key):
	swap = re.compile('Swap:.*').search(key).group()
	print swap

def Split_pid(key):
	pid_info = string.split(key,'cached')
	print pid_info[1] 

try:
	out_top = commands.getoutput('top -d 5 -n 1')
	Mem(out_top)
	Cpu(out_top)
	Task(out_top)
	Swap(out_top)
	Split_pid(out_top)
	
except:
	print "error occured"
