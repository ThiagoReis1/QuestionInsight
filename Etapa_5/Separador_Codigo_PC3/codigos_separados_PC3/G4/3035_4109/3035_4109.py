from math import*
x = float(input("Valor de x: "))
if((0<=x and x<90) or (180<=x and x<270)):
	print(round(sin(radians(x)),4))
elif((90<=x and x<180) or (270<=x and x<360)):
	print(round(cos(radians(x)), 4))
else:
	print("entrada invalida")

