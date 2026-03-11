from math import*

x = float(input("number: "))

if (0 <= x < 90) or (180 <= x < 270):
	y = sin(radians(x))
	print(round(y, 4))

elif (90 <= x < 180) or (270 <= x < 360):
	y = cos(radians(x))
	print(round(y, 4))

else :
	print("entrada invalida")