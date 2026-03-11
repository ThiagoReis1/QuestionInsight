from numpy import*

vetor = array(eval(input("digite o valor:")))
n=size(vetor)
i=0
while n>i:
	if vetor[i] > 80.00:
		desconto=5.0
		vetor[i]=vetor[i]-desconto
	else:
		vetor[i]=vetor[i]
		vetor[i]=round(vetor[i],2)
	i=i+1
vetor1=sum(vetor)
vetor1=round(vetor1,2)
print(vetor1)