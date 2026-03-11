from numpy import *
vetor = array(eval(input("digite a distancias dos lancamentos: ")))
i = 0
k = 0
recorde = 98.48
while(i<size(vetor)):
	if(vetor[i]<recorde):
		k = k + 1
	i = i + 1 
print(recorde)
print(k)