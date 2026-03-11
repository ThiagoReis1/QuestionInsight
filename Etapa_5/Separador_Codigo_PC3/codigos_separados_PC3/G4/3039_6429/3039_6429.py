from math import * 

x = float(input("valor de x: "))


if x < -1 or x > 1:
	print("entrada invalida")
else:
	if -1 <= x <= -0.5 or 0.5 < x <= 1:
		print(round(asin(x),2))
	else:
		print(round(acos(x),2))