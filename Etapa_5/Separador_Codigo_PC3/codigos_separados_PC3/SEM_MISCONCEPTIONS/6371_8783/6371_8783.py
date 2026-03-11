from numpy import *
vetor=array(eval(input("")))
senha=zeros(size(vetor),dtype=int)
for i in range(size(vetor)):
	if vetor[i]==0:
		senha[i]=(9)**2
	else:
		senha[i]=(vetor[i]-1)**2
print(senha)