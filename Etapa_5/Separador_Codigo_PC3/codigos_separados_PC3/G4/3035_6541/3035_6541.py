import math

x = float(input())

	
if(x >= 0 and x < 90.0) or (x >= 180 and x < 270.0):
	x = math.radians(x)
	xsin = math.sin(x)
	print(round(xsin, 4))
	
elif (x >= 90 and x < 180.0) or (x >= 270 and x < 360.0):
	
	x = math.radians(x)
	xcos = math.cos(x)
	print(round(xcos, 4))
		
else:
	print("entrada invalida")