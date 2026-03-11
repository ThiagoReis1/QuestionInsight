from numpy import*
vetor= array(eval(input()))
i=0
soma=0
while(i<size(vetor)):
	if(vetor[i]>=80):
		d = vetor[i]*0.15
		vd = vetor[i] - d
		soma = soma + vd
	else:
		soma = soma + vetor[i]
	i= i + 1
print(round(soma,2))

