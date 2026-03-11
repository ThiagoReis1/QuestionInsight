from numpy import *
x = array(eval(input("Numero sortiados: ")))

saida = zeros(37, dtype=int)
for i in x:
	saida[i] += 1 
print(saida)
	