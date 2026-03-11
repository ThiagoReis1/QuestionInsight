from numpy import*

vetor=array(eval(input("digite o vetor:")))

i=0
positivo=0
while i < size(vetor):
	if vetor[i]>=50:
		i=i+1
	else:
		positivo=positivo+1
		i=i+1
		


v1=array(ones(positivo,dtype=float))
i=0
j=-1
while i < size(vetor):
	if vetor[i]<50.0 or i<size(vetor):
		vetor[i]==vetor[j]
		j=j+1
		print(v1*vetor[j])
	i=i+1
		
	

		
	
		
	
	

		
		