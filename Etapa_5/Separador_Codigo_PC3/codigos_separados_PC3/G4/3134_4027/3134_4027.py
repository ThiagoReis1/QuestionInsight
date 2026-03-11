from numpy import *
vet = array(eval(input("Numeros reais positivos: ")))
i = 0
n = size(vet)
soma = 0
while(i < n):
	soma = soma + (vet[i])**2
	i = i + 1
M = soma/n
M = (M)**0.5
print(round(M, 2))