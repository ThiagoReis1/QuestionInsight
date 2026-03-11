from numpy import *
vet = array(eval(input("digite o vetor:")))
vet1 =array(zeros(2,dtype = int ))
A = min(vet)
B = max(vet)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B
for i in range(size(vet)):
	if (vet[i] >= A and vet[i] <= C):
		vet1[0] = vet1[0] + 1
	elif (vet[i] >= C and vet[i] < D):
		vet1[1] = vet1[1] + 1
print(vet1)