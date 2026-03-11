from numpy import *
vetor = array(eval(input("digite o salto:")))
i = 0
k = 0
recorde = 8.95
while(i < size(vetor)):
	if(vetor[i] > recorde):
		k = k + 1
	i = i +1
print(recorde)
print(k)