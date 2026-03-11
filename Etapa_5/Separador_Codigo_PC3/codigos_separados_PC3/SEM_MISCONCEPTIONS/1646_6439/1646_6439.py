from numpy import *

vetor = array(eval(input("vetor: ")))
 
cont = 0

for i in vetor:
	if i <= 50:
		cont = cont + 1
print(cont)

contagem = zeros(cont, dtype=int)		
j = 0 

for i in range(size(vetor)):
	if vetor[i] <= 50:
		contagem[j] = i
		j = j + 1
print(contagem)

