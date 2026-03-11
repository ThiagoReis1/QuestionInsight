from numpy import*

vet = array(eval(input()))
a=0
i=0


while(a<size(vet)):
	if(vet[a]>80):
		i = i + (vet[a]*0.15)
		
	a = a + 1

print(round(sum(vet)-i,2))
