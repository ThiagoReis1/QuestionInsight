from numpy import*
vetor=array(eval(input("Digite:")))
A=min(vetor)
B=max(vetor)
C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B
cont=zeros(2, dtype=int)
for i in range(size(vetor)):
	if(A<=vetor[i] and C>vetor[i]):
				cont[0] = cont[0] + 1
	elif(D<=vetor[i] and B>vetor[i]):
				cont[1] = cont[1] + 1
print (cont)
		