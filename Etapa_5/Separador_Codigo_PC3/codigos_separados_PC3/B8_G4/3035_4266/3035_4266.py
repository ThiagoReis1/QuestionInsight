from math import*

x = float(input("Digite o valor de x: "))
if(0<=x<=360):
	if(0<=x<=90) or (180<=x<=270):
		fx= sin(radians(x))
		print(round(fx,4))
	elif(90<=x<=180) or (270<=x<=360):
		fx= cos(radians(x))
		print(round(fx,4))
else:
	print("entrada invalida")
