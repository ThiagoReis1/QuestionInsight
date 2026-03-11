from numpy import * 

compra = array(eval(input("Qual o custo dos itens: ")))

i = 0

while(i < size(compra)):
	if(compra[i] > 50):
		compra[i] = compra[i] - ((8/100) * compra[i])
	else:
		compra[i] = compra[i]
	
	i = i + 1
soma = sum(compra)
print(round(soma, 2))