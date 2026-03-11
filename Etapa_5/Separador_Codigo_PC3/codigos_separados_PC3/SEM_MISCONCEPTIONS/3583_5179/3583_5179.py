from numpy import *
compra = array(eval(input("Valores: ")))

cont = 0

while (cont < len(compra)):
	if (compra[cont] > 50):
		compra[cont] = compra[cont] - (compra[cont] * 8/100)
		cont = cont + 1
	else:
		cont = cont + 1
		
x = sum(compra)
print(round(x, 2))