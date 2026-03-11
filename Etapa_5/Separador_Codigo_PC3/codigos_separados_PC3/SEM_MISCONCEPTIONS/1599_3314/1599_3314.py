from numpy import *
item=array(eval(input("Digite o valor: ")))
i = 0
soma = 0
while (i<size(item)):
	if (item[i] > 80.0):
		desconto = item[i]*0.15
		novo_item = item[i] - desconto
		soma = soma + novo_item
	else:
		soma = soma + item[i]
	i = i + 1
print(round(soma,2))
