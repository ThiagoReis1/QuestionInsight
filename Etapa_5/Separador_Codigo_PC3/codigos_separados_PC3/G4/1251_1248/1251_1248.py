from numpy import*
from math import*

vet = array(eval(input("Digite o vetor: ")))
x = array(zeros(2,dtype = int))

A = min(vet)
B = max(vet)

C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B


for i in range(size(vet)):
	if((vet[i] >= A) and (vet[i] < C)):
		x[0] = x[0] + 1
		
		
for i in range(size(vet)):
	if((vet[i] >= D) and (vet[i] < B)):
		x[1] = x[1] + 1
		
print(x)
			
		
		



