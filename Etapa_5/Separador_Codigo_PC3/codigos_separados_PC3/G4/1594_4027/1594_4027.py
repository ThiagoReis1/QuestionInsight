from numpy import *
vet = array(eval(input("Insira o vetor de danos: ")))
soma = 0
n = size(vet)
for i in range(n):
	soma = soma + vet[i]*(i + 1)
print(soma)