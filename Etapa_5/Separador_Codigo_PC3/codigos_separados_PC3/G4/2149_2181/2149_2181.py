from numpy import *
vet = array(eval(input("Digite um vetor de notas: ")))
vet1 = array(eval(input("Digite um segundo vetor de notas: ")))

v = zeros(size(vet), dtype = float)

soma = 0
for i in range(size(vet)):
	v[soma] = vet[i] + vet1[i]
	soma = soma + 1
print(v)

cont = 0
for j in range(size(vet1)):
		if(vet[j] + vet1[j] >= 12):
			cont = cont + 1
print(cont)