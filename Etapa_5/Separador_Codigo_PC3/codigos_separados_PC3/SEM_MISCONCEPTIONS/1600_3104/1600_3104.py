from numpy import*
itens = array(eval(input("")))
i = 0
valor = 0 

while(i < size(itens)):
	if(itens[i]>80):
		valor = valor + itens[i] - itens[i]*15/100
	else:
		valor = valor + itens[i]
	i = i + 1 

print(round(valor,2))