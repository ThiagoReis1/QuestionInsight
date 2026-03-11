from numpy import*
vet = array(eval(input()))
i = 0 #INDICE PARA O VETOR VAZIO
c = 0 #CONTADOR DE NUMEROS IMPARES
for x in range(0 , size(vet)):
	if vet[x] % 2 == 1:
		c += 1
vet1 = zeros(c, dtype=int)
for x in range(0, size(vet)):
	if vet[x] % 2 == 1:
		vet1[i] += x
		i += 1
print(c)
print(vet1)
