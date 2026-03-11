import math
x = float(input("digite o valor de x: "))
if x <= -1  or x >= 1:
	f = abs(x)**(1/2)
	print(round(f,2))
elif -1 < x < 0 or 0 < x < 1:
	f = (abs(x))
	print(round(f,2))
elif x == 0:
	print("0")