from numpy import*

compras = array(eval(input("Digite: ")))

i = 0
j = 0

while(i < size(compras)):
	if compras[i] > 80:
		compras[i] = compras[i] - compras[i] * 0.15
	j = compras[i] + j
	i = i + 1
	
print(round(j, 2))