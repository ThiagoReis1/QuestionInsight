from numpy import* 

vetor = array(eval(input("digite o numero: ")))
i = 0
n = max(vetor)

while(vetor[i] != max(vetor)):
	i=i+1
print(i)