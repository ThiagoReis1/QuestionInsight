from numpy import*

compra = array(eval(input("Valores das compras:")))
k = 0
dsc = 0

while (k< size(compra)):
	if compra[k] > 200:
		dsc = dsc + compra[k]*0.15
	k = k + 1
	total = sum(compra) - dsc
print(round(total,2))

