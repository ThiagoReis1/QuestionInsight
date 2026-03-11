from numpy import *

vet = array(eval(input("Digite um numero: ")))

n = zeros(size(vet), dtype=float)

cont = 0

for i in range(size(vet)):
	if (vet[i] > 0):
		cont = cont + 1
	elif (vet[0] > 0):
		vet[0] = vet[0] + 1
	
m = ((vet[i] ** 2 + vet[n - 1] ** 2) / n) ** 1/2

print(round(m, 2))