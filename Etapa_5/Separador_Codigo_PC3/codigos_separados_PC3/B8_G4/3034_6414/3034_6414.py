from math import *
x = float(input("numero: "))
y = x

while(-4<=y<4):
	if (-4<=y< 0):
		fx = abs(y)**(1/2)
		print(round(fx, 4))
	elif (y == 0):
		fx = 0
		print(round(fx, 4))
	elif (0<y<=4):
		fx = (y**(1/2))
		print(round(fx, 4))
else:
	print("entrada invalida")