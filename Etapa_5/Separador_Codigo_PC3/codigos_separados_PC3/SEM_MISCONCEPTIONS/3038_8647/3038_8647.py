from math import *

x = float(input("Qual o valor de x?: "))

if (x <= -1) or (x >= 1):
	calculo = abs(x**(1/2))
	
elif (-1 < x < 0) or (0 < x < 1):
	calculo = abs((x))
	
else:
	(x == 0)
	calculo = 0
	
print(round(calculo, 2))

