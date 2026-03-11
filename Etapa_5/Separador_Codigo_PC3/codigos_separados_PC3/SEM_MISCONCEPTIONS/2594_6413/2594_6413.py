from numpy import *

x = array(eval(input("Demandas: ")))
ponto_c = x[0]
saida = []

for i in range(size(x)):
	if x[i]>ponto_c:
		saida.append(i)

for j in range(size(saida)):
	print(saida[j])
print(size(saida))