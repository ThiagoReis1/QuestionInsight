from numpy import*
from math import*


x = float(input("x"))

if x == 0:
	fx=0
if (x > -1 and x < 0) or (x<1 and x>0):
	fx=abs(x)
if (x<= -1) or (x>=1):
	fx= abs(x**(1/2))

print(round(fx,2))