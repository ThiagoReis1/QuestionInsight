from numpy import *

nota = array(eval(input("")))

aprovados = 0
val_indice = 0

for i in range (len(nota)):
	if nota[i] >= 5:
		aprovados += 1
		
vet = zeros(aprovados, dtype=int)	
j = 0
for i in range  (len(nota)):
	if nota[i] >= 5:
		vet[j] = i
		j = j+1
		
	
		
print(aprovados)
print(vet)
