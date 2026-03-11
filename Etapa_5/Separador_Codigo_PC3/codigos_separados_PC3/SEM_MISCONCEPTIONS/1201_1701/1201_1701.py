from numpy import*
minimo = 0
maximo = 40
vetor = array(eval(input("Digite o vetor:")))
i = 0
q = 0
while(i < size(vetor)):
	if((minimo < vetor[i]) and (vetor[i] < maximo)):
		q = q + 1
	i = i + 1
vetor2 = zeros(q, dtype = float)
i = 0
i2 = 0
while(i < size(vetor)):
	if((minimo < vetor[i]) and (vetor[i] < maximo)):
		vetor2[i2] = vetor[i]
		i2 = i2 + 1
	i = i + 1
print(vetor)