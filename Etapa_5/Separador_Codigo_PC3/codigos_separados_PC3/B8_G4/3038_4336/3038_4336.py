x = float(input("Valor de x: "))

from math import*
if (x <= -1) or (x >= 1):
	print(round(x**(1/2) , 2))
elif ((x > -1) or (x < 0)) or ((x > 0) or (x < 1)):
	print(abs(round(x , 2)))
elif (x == 0):
	print(round(0 , 2))
	