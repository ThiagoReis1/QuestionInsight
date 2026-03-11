from math import*

x = float(input(""))

if((x <= (-1)) or (x >= 1)):
	g = print(round(x**2, 4))
				 
elif(((-1) < x) and (x < 0) or (0 < x) and (x < 1)):
	g = print(round(x, 4))
			 
elif ( x == 0):
	g = print(round(1, 4))