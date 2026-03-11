x=float(input())

from math import *

if x<=0:
	f=0
elif x>0 and x<=1:
	f= 1
elif 1<x and x<=2:
	f= sqrt(x)
elif x>2:
	f= x**(1/3)
print(round(f,4))