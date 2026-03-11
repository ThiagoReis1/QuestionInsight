from numpy import *

me=input()

idc=0
tt=0

M=7.25
P=4.75
R=3.50

while idc<len(me):
	if me[idc]== 'M':
		tt+=7.25
	elif me[idc]=='P':
		tt+=4.75
	elif me[idc]== 'R':
		tt+=3.50
	idc+=1
print(round(tt,2))