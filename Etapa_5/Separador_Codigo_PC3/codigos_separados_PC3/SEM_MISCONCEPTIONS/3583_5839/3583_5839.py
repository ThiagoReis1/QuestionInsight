from numpy import *

custo = array(eval(input("Digite o valor gasto nas compras: ")))
x = size(custo)

valor = 0 
i = 0

while (i < x):
	if (custo[i] > 50.00):
		valor = valor + (custo[i] - custo[i] * 0.08)
		i = i + 1
	else:
		valor = valor + custo[i]
		i = i + 1
	
print(round(valor,2))