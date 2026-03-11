from numpy import *
custo = array(eval(input("Custo de itens: ")))
i = 0
desconto = 0
for i in (range(size(custo))):
	if custo [i] > 90:
		desconto = desconto -6.50 
		desconto = desconto + custo[i]
	else:
		desconto = desconto + custo[i]
print(round(desconto, 2))