from numpy import *

vet = array(eval(input("aprovados: ")))

cont= 0
for i in range(size(vet)):
	if(vet[i] >= 70):
		cont = cont + 1
print(cont)

valor =zeros(cont, dtype=int)

j= 0

for i in range(size(vet)):
	if (vet[i] >= 70):
		valor[j]= i
		j = j + 1
		
print(valor)
	