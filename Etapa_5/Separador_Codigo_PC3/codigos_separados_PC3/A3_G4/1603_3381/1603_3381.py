from numpy import*

vetor= array(eval(input()))
tam=size(vetor)
soma=0
i=0 

while 1 <= vetor[i] < 4:
	if vetor[i]==1:
		soma=soma + 80
		i=i+1
	elif vetor[i]==2:
		soma=soma + 40
		i=i+1
	else:
		soma = soma + 20
		i=i+1

print(soma)		
	