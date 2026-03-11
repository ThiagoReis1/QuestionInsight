from numpy import *
vetor = array(eval(input("Digite as distâncias dos lancamentos: ")))
i = 0
k = 0
recorde = 74.08
while(i<size(vetor)):
	if(vetor[i]<recorde):
		k = k + 1
	i = i + 1
print(recorde)
print(k)