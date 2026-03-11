from numpy import *

entrada = eval(input())

cont_impar = 0

for i in range(len(entrada)):
	if entrada[i]%2 != 0:
		cont_impar += 1
		
vetor = zeros(cont_impar, dtype=int)
j = 0
	
for i in range(len(entrada)):
	if entrada[i]%2 != 0:
		vetor[j] = i
		j = j+1
		
	
print(cont_impar)
print(str(vetor).replace(",",""))