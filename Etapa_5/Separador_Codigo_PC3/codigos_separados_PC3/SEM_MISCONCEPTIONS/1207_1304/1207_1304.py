from numpy import *
vetor = array(eval(input("vetor: ")))
recorde = 98.48
i = 0
n = 0
while(i < size(vetor)):
	if (vetor[i] > recorde):
		n = n + 1
	i = i + 1
print(recorde)
print(n)