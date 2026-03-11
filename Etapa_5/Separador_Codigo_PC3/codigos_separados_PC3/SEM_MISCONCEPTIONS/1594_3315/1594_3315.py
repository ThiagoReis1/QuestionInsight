from numpy import*

vetor = array(eval(input()))

dano_total=0
i=0

while(i<size(vetor)):
	dano_total = dano_total + vetor[i]*(i+1)
	i=i+1
	
print(dano_total)

