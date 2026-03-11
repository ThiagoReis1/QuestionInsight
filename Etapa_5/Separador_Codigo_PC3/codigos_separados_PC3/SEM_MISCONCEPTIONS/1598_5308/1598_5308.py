# SE COMPRA TOTAL PASSAR DE 90, DESCONTA 6.50 DO TOTAL
#A CADA ITEM ACIMA DE 90

from numpy import*

custo = array(eval(input("itens: ")))

i = 0

while i < size(custo):
	if custo[i] > 90:
		custo[i] = custo[i] - 6.50
		
	else:
		custo[i] = custo[i]
		
	i = i + 1
	
print(round(sum(custo), 2))