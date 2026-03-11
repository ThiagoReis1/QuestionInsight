from math import*

x = float(input("Valor de x: "))
fx = float(asin(-1<=x<-1/2) or (1/2<x<=1))
fy = float(acos(-1/2)<=x<=1/2)

if (x <= -1) and (x < -1/2) or (x < 1/2) and (x <= 1):
	resultado = fx
	Resultado = degrees(fx)
elif (x <= -1/2) and (x <= 1/2):
	resultado = fy
	Resultado = degrees(fy)
else:
	print("Entrada invalida")

print(round(Resultado,2))
	