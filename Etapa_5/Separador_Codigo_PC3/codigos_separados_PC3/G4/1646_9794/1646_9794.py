from numpy import *
v = array(eval(input("insira o vetor: ")))
cont = 0
for e in v:
	if e <= 50:
		cont = cont + 1
print(cont)
			 
saida = zeros(cont, dtype=int)
pos = 0
for i in range(size(v)):
	if v[i] <= 50:
		saida[pos] = i
		pos = pos + 1
print(saida)