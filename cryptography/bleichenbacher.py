# -*- coding: utf-8 -*-

def get_ST10(sn):
	tmp = int('0x'+sn,16)
	print "(10)" + str(tmp) 
	print "(16)" + hex(tmp*(16**8))
	return tmp*(16**8) 

def get_FR16(sn):
	st = get_ST10(sn)
	M = st
	a = 2**80 - M
	print "this is a "
	print a
	#print int('0xffffe93cfe8900000000',16)
	#return a % 3
	return a 

def main(sn):
	a = get_FR16('16c30177')
	s = 2**395 - (a/3)*(2**42) 
	print hex(s) 
	print hex(s^3)	


'''	fr = b
	chk = 2**32
	while fr > chk:
		fr -=3
		print fr
	return fr
'''
main('16c30177')

	
