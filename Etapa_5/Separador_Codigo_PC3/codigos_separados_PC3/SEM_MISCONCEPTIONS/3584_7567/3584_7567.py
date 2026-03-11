from numpy import*
custo = array(eval(input("")))
i = 0
total = custo
while(i < size(custo)):
	if(custo[i] > 200):
		total[i] = total[i] - (total[i] * 15 / 100)
		i = i + 1
	else:
		total[i] = total[i]
		i = i + 1
compra = sum(total)
print(round(compra, 2))