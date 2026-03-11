from numpy import*
custo = array(eval(input("Valores dos itens: ")))
i = 0 #contador vetor custo
k = 0 #contador preço > 80

while i < size(custo):
	if custo[i] > 80.0:
		k = k + custo[i]*0.85
	else:
		k = k + custo[i]
	i = i + 1	

print(round(k, 2))
