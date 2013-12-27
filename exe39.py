#/bin/env python
#-*- encoding:UTF-8 -*-

#create a mapping of state to abbreviation 
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
	}

#create a basic set of states and some cities in them 
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	}

#add some more cities 
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out some cities 
print '-' * 10
print "NY State has :", cities ['NY']
print "OR State has :", cities ['OR']

#print some states 
print '-' * 10
print "Michigan's abbreviation is :",states ['Michigan']  #获取字典值的方法，用下标文字
print "Florida's abbreviation is :",states ['Florida']

#do it by using the state then cities dict 
print "-" * 10
print "Michigan's has :",cities [states ['Michigan']]  #获取第二层字典值的方法
print "Florida has :",cities [states ['Florida']]

#print every state abbreviation 
print '-' * 10
for state , abbrev in states.items():           #字典的遍历输出是无序的，以后都是
	print "%s is abbreviated %s " % (state, abbrev)

#print every city in state 
print '-' * 10
for abbrev ,city  in cities.items():
	print "%s has the city %s " % (abbrev, city )

#now do both at the same time
print '-' * 10
for state ,abbrev in states.items():
	print "%s state is abbreviated %s and has city %s " % (state,abbrev ,cities[abbrev])                 #遍历两个相关联字典的方法

print '-' * 10
#safety get a abbreviation  by state that might not be there 
state  = states.get('Texas',None)  #获取某一字典值的方法get

if not state :
	print "sorry , no texas ."

#get a city with a default value 
city = cities.get("TX", "Does Not Exist")  #注意如果无法获取时返回"Does Not Exist"
print "The city for the state 'TX' is : %s " % city 

