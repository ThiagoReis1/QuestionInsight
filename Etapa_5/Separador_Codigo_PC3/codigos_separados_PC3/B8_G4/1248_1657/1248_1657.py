#Universidade Federal do Amazonas
#25/08/2016
# Matricula 21553775

from numpy import*
v = array(eval(input("Digite o vetor")))
vet = zeros(2, dtype = int)
A = min(v)
B = max(v)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

for i in range(size(v)):
	if((v[i] > C or v[i] ==C) and v[i] < D):
		vet[0] = vet[0] + 1
	elif ((v[i] > D or v[i] == D) and v[i] < B):
		vet[1] = vet[1] + 1
print(vet)