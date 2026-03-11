from numpy import*
from math import*

vet = array(eval(input("digite o vetor: ")))
x = array(zeros(2, dtype = int))

A = min(vet)
B = max (vet)

C = 0.75 * A + 0.25* B
D = 0.25* A + 0.75* B
for i in range(size(vet)):
	if(vet[i]>= C and vet[i]<D):
		x[0] = x[0] + 1
for i in range(size(vet)):
	if(vet[i]>=D and vet[i]< B):
		x[1] = x[1] + 1
print(x)
