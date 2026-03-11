from numpy import*

vetor = array(eval(input()))
i=0
tamanho = size(vetor)

while i < tamanho :
	if(vetor[i]>50.00):
		vetor[i]=vetor[i]-vetor[i]*8/100
	i=i+1
print(round(sum(vetor),2))