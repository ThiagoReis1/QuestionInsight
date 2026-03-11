x = float(input("valor de x: "))
from math import*
if (x <= -1) or (x > 1):
	f = abs(x**(1/2))
elif (x > -1) and (x < 0) or (x > 0) and (x < 1):
	f = abs(x)
elif (x == 0):
	f = 0
print(round(f, 2))