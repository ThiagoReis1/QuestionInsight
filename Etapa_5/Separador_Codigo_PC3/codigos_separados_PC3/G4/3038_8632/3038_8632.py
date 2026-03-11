from math import *

x = float(input("x: "))

if x <= -1 or x >= 1:
	re = abs(x**(1/2))
elif -1 < x < 0 or 0< x< 1:
	re = abs(x)
else:
	re = 0

print(round(re, 2))