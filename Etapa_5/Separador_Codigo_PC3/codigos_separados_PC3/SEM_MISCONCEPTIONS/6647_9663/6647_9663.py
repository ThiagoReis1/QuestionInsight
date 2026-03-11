from numpy import*

vetor = array(eval(input("Digite os valores para o vetor: ")))
peso = [2,1,5]

i = 0
soma = 0

while i < size(vetor):
	soma = soma + vetor[i] * peso[i] 
	media = soma / sum(peso)
	i = i + 1

print(round(media,2))
