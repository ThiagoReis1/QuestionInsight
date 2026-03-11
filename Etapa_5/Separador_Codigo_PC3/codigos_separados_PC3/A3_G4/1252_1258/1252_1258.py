from numpy import*
from math import*
vet = array(eval(input("digite o vetor")))
x = array(zeros(2,dtype = int))
cont = 0
A = min(vet)
B = max(vet)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B
for i in range(size(vet)):
	if((vet[i]>= A) and (vet[i]<=C)):
		x[0] = x[0] + 1
for i in range(size(vet)):
	if(vet[i]>= C and vet[i]<=D):
		x[1] = x[1] + 1
print(x)		
