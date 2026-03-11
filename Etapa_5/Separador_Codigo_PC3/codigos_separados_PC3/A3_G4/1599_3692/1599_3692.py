from numpy import*
vet = array(input())
i=0
while i < size(vet): 
	if vet[i] > 80:
		desc = vet[i] - vet[i]*0.15
	i=i+1	
ctotal = sum(vet)
print(round(ctotal,2))