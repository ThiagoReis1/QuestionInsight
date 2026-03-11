from numpy import*

vet = array(eval(input("diga o vetor:")))

i = 0
soma = 0
pesos = [1, 2, 3]

while i < size(vet):
	soma =  soma + (vet[i] * pesos[i])
	i+=1

nota = soma / sum(pesos)
print(round(nota,2))