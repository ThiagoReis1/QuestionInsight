from numpy import *
vetor = array(eval(input("Informe aqui os valores dos vetores:")))
r=74.08
i=0
q=0
while(i<size(vetor)):
	if(vetor[i]<r):
		q=q+1
	i=i+1
print(r)
print(q)