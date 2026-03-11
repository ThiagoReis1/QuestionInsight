import math
x=float(input("Digite um numero: "))
if x<= -1 or x>=1:
	resultado= math.sqrt(abs(x))
	print(round(resultado,2))
elif -1<x<0 or 0<x<1:
	resultado= abs(x)
	print(round(resultado,2))
else:
	resultado= 0
	print(round(resultado,2))
	