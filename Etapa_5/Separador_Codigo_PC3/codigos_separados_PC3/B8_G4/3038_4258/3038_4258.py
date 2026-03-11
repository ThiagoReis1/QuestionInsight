x = float(input("Valor de X: "))

from math import *

if(x <= -1) or (x >= 1):
	f = sqrt(abs(x))
	print(round(f, 2))
	
elif(-1 < x < 0) or (0 < x < 1):
	f = abs(x)
	print(round(f, 2))
	
elif(x == 0):
	f = 0
	print(f)