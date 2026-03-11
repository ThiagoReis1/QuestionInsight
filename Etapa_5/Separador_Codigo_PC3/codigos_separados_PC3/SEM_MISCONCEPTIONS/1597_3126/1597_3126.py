from numpy import*

compra = array(eval(input("valor do item: ")))
desconto = 5.0

i = 0
cont = 0

while (i < size(compra)):
	if (compra[i] > 80.0):
		cont = cont + 1
	i = i + 1

total = sum(compra) - (desconto * cont)
	
print(round(total, 2))
	