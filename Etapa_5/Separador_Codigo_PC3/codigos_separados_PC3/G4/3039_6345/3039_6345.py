import math
x = float(input("x: "))


if (x >= -1) and (x < -0.5) or (x > 0.5) and (x <= 1):
	print(round(math.asin(x),2))
	
elif (x >= -0.5) and (x <= 0.5):
	print(round(math.acos(x),2))
	
else:
	print("entrada invalida")