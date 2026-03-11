from math import *

x = float(input())

if (x==0):
	res = 0	
elif(x<=-1 or x>= 1):
	res = abs(x)**(1/2)
elif((x>-1 and x<0) or (x>0 and x<1)):
	res = abs(x)
	
print(round(res, 2))