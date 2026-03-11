from numpy import *

custo = array(eval(input("insira um vetor de custo: ")))

for i in range(size(custo)):
	if custo[i]> 80.0:
		custo[i] -= 5.00
	custo_total = (sum(custo))
		
print(round(custo_total,2)) 