from numpy import *
s = 2.5
vetor = array(eval(input("Informe o vetor: ")))
i = 0
cont = 0

while(i < size(vetor)):
	if(vetor[i] < s):
		cont = cont + 1
	i = i + 1
print(s)
print(cont)