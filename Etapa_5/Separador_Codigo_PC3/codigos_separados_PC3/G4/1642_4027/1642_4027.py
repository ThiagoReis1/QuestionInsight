from numpy import*
vet = array(eval(input("Insira o vetor: ")))
n = size(vet)
q = 0
for i in range(n):
	if(vet[i]%5 == 0):
		q = q + 1
vet_saida = zeros(q, dtype = int)
j = 0
for i in range(n):
	if(vet[i]%5 == 0):
		vet_saida[j] = i
		j = j + 1
print(q)
print(vet_saida)