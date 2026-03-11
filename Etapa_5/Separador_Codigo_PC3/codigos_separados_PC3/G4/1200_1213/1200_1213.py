from numpy import*
vet=array(eval(input("digite as temperaturas:")))
i=0
z=0
while(i<size(vet)): 
	if(vet[i]>0):
		z=z+1
	i=i+1	
vet2 = array(zeros(z,dtype=float))
j=0
x=0
while(j<size(vet)): 
	if(vet[j]>0):
		vet2[x]=vet[j]
		x=x+1
	j=j+1
print(vet2)
