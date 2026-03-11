from numpy import*
vet=array(eval(input("digte a compra")))

i=0
while(size(vet)>i):
	if(vet[i]>80):
		x=(vet[i]*15)/100
		vet[i]=vet[i]+x
	i=i+1
		
print(round(sum(vet),2))