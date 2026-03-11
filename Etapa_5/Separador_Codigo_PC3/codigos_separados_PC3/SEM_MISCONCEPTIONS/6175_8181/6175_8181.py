from math import*
x = float(input("informe o valor de x: "))
if(0 <= x) and (x <= 4):
	valor= x**(1/2)
	print(round(valor,4))
elif(-4<=x) and (x<0):
	valor= abs(x)**(1/2)
	print(round(valor,4))
else:
	print("entrada invalida")
