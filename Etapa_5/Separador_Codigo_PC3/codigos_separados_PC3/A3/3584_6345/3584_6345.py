from numpy import *

valor = array(eval(input("valor: ")))
i = 0
desconto = 0
total = 0

for i in range(size(valor)):
	if valor[i] > 200:
		desconto = valor[i] * 0.85
		total = total + desconto
		
	else:
		total = total + valor[i]
print(round(total,2))