#/bin/env python
#-*- encoding:UTF-8 -*-

#create a mapping of hundred  to decimal  
hundred  = {
	'100': '10*10',
	'200': '20*10',
	'300': '30*10',
	'400': '40*10',
	'500': '50*10'
	}

#create a basic set of hundred and some decimal in them 
decimal  = {
	'30*10': '30',
	'50*10': '50',
	'20*10': '20',
	'40*10': '40',
	'10*10': '10'
	}
print decimal[hundred['400']]

for f,a in decimal.items():
	print "%s decimal by decimal %s" % (f,a)
print '*' * 20

for f,a in hundred.items():
	print "%s hundred by hundred %s "% (f,a)

for f,a in hundred.items():
	print "%s hundred to decimal %s and has %s" % (f,a,decimal[a])



