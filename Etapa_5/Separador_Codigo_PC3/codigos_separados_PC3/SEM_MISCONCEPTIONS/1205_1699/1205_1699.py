from numpy import *

i = 0
recorde= 8.95
k = 0
vetor = array(eval(input("Informe os valores dos saltos: ")))

while(i < size(vetor)):
	if (vetor[i] > recorde):
		k = k + 1
	i = i + 1

print(recorde)
print (k)