import math 

x = float(input(" "))

if ((x <= -1) or (x >= 1)):
	print(round(abs(x)**0.5, 2))
elif ((-1 < x < 0) or (0 < x < 1)):
	print(round(abs(x), 2))
elif ((x == 0)):
	print(round(0, 2))