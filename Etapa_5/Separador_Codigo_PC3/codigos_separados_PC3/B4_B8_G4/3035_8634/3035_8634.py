from math import radians, sin, cos
x = float(input("Valor de x (graus): "))
senx = sin(radians(x))
cosx = cos(radians(x))
if x < 0 or x >= 360:
	print("entrada invalida")
else:
	if 0 <= x < 90:
		print(round(senx, 4))
	elif 90 <= x < 180:
		print(round(cosx, 4))
	elif 180 <= x < 270:
		print(round(senx, 4))
	elif 270 <= x < 360:
		print(round(cosx, 4))