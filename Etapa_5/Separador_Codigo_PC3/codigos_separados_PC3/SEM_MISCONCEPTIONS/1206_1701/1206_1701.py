from numpy import *
vetor = array(eval(input("Digite as distâncias: ")))
i = 0
s = 0
while(i < size(vetor)):
	if(vetor[i] < 8.95):
		s = s + 1
	

i = i + 1
print(vetor[i])
print(s) 