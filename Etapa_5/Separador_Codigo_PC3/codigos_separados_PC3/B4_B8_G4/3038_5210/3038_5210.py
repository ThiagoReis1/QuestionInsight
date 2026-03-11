from math import * 
x = float(input(""))



if ((x <= -1) or (x >= 1)):
	a = abs(x) ** (1/2)
	print(round(a, 2))
elif ((x > -1) and (x < 0)):
	a = abs(x)
	print(round(a, 2))
elif ((x > 0) and (x < 1)):
	a = abs(x)
	print(round(a, 2))
elif (x == 0):
	a = 0
	print(round(a, 2))

	