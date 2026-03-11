from numpy import*

itens = array(eval(input('Vetor de custo: ')))

i = 0
qtdesc = 0
desc = 5.0
compra = 0
while i < size(itens):
	if itens[i] > 80.0:
		qtdesc = qtdesc + 1
		compra = sum(itens) - desc * qtdesc
	else: 
		compra = sum(itens)
	i = i + 1
print(round(compra, 2))
		