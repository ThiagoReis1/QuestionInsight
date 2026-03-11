from numpy import *

custo = array(eval(input("Qual o vetor das compras: ")))


i = 0
total = 0
for i in range(size(custo)):
	if (custo[i] <= 80):
		total = total + custo[i]
	
	else:
		total = custo[i] - (0.15 * custo[i]) + total
		
print(total)
		