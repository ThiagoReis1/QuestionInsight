from numpy import *
vetor = array(eval(input("insira as temperaturas:")))
i = 0
taxa1 = -60
taxa2 = 60
while (i<=size(vetor)):
	if (vetor[i] < taxa1):
		vetor2 = array(vetor.remove[i])
	while(vetor2[i] <= size(vetor2)):
		if(vetor2[i]>taxa2):
			vetor3 = array(vetor2.remove[i])
		i = i+1
print(vetor3)