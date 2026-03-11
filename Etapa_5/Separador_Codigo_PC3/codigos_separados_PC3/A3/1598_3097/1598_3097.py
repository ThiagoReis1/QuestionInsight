from numpy import*
vetor=array(eval(input("digite o vetor de custos: ")))
i=0
n=size(vetor)
total=0

while(i<n):
	if(vetor[i]>80):
		total=sum(vetor)-5
	else:
		total=sum(vetor)
	i=i+1
print(round(total,2))


	
	
	
	
