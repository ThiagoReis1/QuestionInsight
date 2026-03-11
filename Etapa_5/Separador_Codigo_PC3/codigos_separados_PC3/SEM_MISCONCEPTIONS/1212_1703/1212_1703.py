# Hanna Soares Rodrigues - 21650885

from numpy import*

vetor = eval(input("digite o vetor: "))

record = 307
print(record)

vetor1 = zeros(tamanho,dtype=int)
a = 0
b = 0

while (vetor[a] > vetor1[b]):
	c = 0
	if(vetor[a] < 307):
		vetor1 = zeros(tamanho,dtype=int)
		tamanho = tamanho + 1
		c = c + 1
	a = a + 1
	b = b + 1
	
print(tamanho)
	
	