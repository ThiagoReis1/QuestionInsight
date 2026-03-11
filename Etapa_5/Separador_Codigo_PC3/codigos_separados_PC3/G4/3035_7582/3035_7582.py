from math import*
x = float(input("x "))
if ((x >= 0) and (x < 90)) or ((x >= 180) and (x < 270)):
	fx = sin(radians(x))
	print(round(fx,4))
elif ((x >= 90) and (x < 180) or (x >= 270) and (x < 360)):
	fx = cos(radians(x))
	print(round(fx,4))
else:
	print("entrada invalida")