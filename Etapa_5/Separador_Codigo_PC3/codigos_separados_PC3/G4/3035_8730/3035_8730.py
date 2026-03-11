from math import*
x = float(input("valor do X:"))
if (x>=0 and x<90) or (x>=180 and x<270):
	v = sin(radians(x))
	print(round(v,4))
elif(x >= 90 and x< 180) or (x >= 270 and x < 360):
	v = cos(radians(x))
	print(round(v,4))
else:
	print("entrada invalida")
	