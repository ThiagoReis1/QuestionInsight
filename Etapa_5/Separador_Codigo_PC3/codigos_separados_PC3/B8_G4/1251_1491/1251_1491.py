from numpy import *
vet = array(eval(input("Insira o vetor:")), dtype = float)
a = min(vet)
b = max(vet)
c = (0.7 * a) + (0.3 * b)
d = (0.4 * a) + (0.6 * b)

x = array(zeros(2, dtype = int))

for i in range(size(vet)):
	if (vet[i] >= c and vet[i] < d):
		x[0] = x[0] + 1
	elif (vet[i] >= d and vet[i] < b):
		x[1] = x[1] + 1
print(x)