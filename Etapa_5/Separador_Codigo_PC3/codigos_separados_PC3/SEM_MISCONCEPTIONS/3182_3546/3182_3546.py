from numpy import *
trincas = array(eval(input()), dtype=int)

saida = zeros(10, dtype=int)

for i in range(0, size(trincas), 3):
	if(trincas[i] == trincas[i+1] and trincas[i] == trincas[i+2]):
		saida[trincas[i]] = saida[trincas[i]] + 1

print(saida)