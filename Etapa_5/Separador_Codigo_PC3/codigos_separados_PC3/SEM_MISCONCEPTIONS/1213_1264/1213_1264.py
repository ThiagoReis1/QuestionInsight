from numpy import*

vetor=array(eval(input("vetor pesos:")))

n=0
cont=0

while(n < size(vetor)):
	if( vetor[n] > 217):
		cont=cont + 1
	n=n+1	

print(217)
print(cont)
