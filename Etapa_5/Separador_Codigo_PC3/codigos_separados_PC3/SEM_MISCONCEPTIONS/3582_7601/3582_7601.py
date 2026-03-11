from numpy import*

vetor = array(eval(input("Digite um vetor com o custo dos itens: ")))


i = 0
soma = 0
while i < size(vetor):
	if vetor[i] > 160.0:
		soma = soma + (vetor[i] - 25.0)
	else:
		soma = soma + vetor[i]
	i = i + 1

print(round(soma,2))