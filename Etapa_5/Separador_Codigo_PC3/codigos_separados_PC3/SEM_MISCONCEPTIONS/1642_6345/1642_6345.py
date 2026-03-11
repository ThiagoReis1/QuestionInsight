from numpy import *

vet = array(eval(input("alunos: ")))
n = 0
indice = 0

for i in range(size(vet)):
	if vet[i] % 5 == 0:
		n = n + 1
		
saida = zeros(n, dtype=int)

for i in range (size(vet)):
	if vet[i] % 5 == 0:
		saida[indice] = i
		indice += 1

print(n)
print(saida)
