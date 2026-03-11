from math import *

x = int(input())
k = int(input())
if(k % 2 == 0):
	a = 1
else:
	a = 1
	k = ( k * 2) + 1
	e= 0
while(k >= 1):
	b =factorial(k)
	c = ( x ** k)
	c = a * (c / b)
	e = e + c
print(round(e,9))
