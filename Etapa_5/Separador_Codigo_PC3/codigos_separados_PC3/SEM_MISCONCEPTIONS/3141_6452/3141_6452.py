from numpy import*
vetor=array(eval(input('digite o vetor pls: ')))
soma=0
for i in range (size(vetor)):
	soma=soma+vetor[i]**(1/6)
med=(soma/size(vetor))**6
print(round(med,2))