from numpy import*  
vet= array(eval(input("")))
i=0
while(i<size(vet)):
	vet[i]=vet[i]**1/3
	i= i+1
vet= (sum(vet)/size(vet))**3
print(round(vet,2))
	


