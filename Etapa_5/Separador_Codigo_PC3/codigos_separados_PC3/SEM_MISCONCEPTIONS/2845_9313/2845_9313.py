from numpy import*

vetor=array(eval(input("insira o vetor:")))
vetor2=zeros(size(vetor),dtype=int)

for i in range(size(vetor)):
	if vetor[i]==9:
		vetor2[i]=0
	else:
		vetor2[i]=vetor[i]+1
print(vetor2)
	