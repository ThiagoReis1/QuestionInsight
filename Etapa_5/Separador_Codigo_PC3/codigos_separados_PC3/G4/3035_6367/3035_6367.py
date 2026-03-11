from math import*
x=radians(float(input("Insira o valor de x: ")))
v1=radians(0)
v2=radians(90)
v3=radians(180)
v4=radians(270)
v5=radians(360)

if v1<=x<v2 or v3<=x<v4:
	resultado=sin(x)
	print(round(resultado,4))
	
elif v2<=x<v3 or v4<=x<v5:
	resultado=cos(x)
	print(round(resultado,4))
	
else:
	print("entrada invalida")