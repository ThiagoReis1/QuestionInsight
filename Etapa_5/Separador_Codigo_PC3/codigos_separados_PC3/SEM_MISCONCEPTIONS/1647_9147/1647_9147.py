from numpy import *

disci = array(eval(input("insira a frequencia das disciplinas: ")))
cont = 0

for i in range(size(disci)):
	if	disci[i] >= 70:
		cont += 1
print(cont)

pares = zeros(cont, dtype=int)
j = 0

for i in range(size(disci)):
	if	disci[i] >= 70:
		pares[j] = i
		j += 1
print(pares)