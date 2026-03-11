from numpy import*

vetor = array(eval(input()))

M = 0

for i in range(size(vetor)):
	if (vetor[i]>=2000.0):
		M=M+1
vetor2 = zeros(M,dtype=int)
aux=0

for i in range(size(vetor)):
	if(vetor[i]>=2000.0):
		vetor2[aux]=i
		aux=aux+1
		
print(M)
print(vetor2)