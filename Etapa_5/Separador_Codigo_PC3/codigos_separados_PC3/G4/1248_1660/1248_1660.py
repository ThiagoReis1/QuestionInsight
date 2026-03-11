from numpy import *
vet = array(eval(input("insira o vetor: ")))
vet1 = array(ones(2, dtype = int))
for i in range (0, size(vet)):
	a = min(vet)
	b = max(vet)
c = (0.75 * a) + (0.25 * b)
d = (0.25 * a) + (0.75 * b)

x1 = 0
for i in range (0, size(vet)):
	if (vet[i] >= c and vet[i] < d):
		x1 = x1 + 1
x2 = 0
for i in range (0, size(vet)):
	if (vet[i] >= d and vet[i] < b):
		x2 = x2 + 1

vet1[0] = x1
vet1[1] = x2
print(vet1)