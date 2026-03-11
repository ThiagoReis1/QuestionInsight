from math import *

x = float(input(""))

if(x >= -4) and (x < 0):
	f = x ** (1/2)
	print(round(abs(f), 4))
elif(x >= 0) and (x <= 4):
	f = x ** (1/2)
	print(round(f, 4))