from numpy import*

vetor= array(eval(input()))

soma=0
i=0

while i<size(vetor):
	soma=soma+vetor[i]*(i+1)
	i=i+1
	
print(soma)