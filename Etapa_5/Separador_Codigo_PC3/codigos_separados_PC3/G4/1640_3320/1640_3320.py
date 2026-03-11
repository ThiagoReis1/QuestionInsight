from numpy import*
vet=array(eval(input("")))

nimpar=0
for i in range(size(vet)):
	if vet[i]%2!=0:
		nimpar=nimpar+1
		
print(nimpar)
vet2= zeros(nimpar,dtype=int)
j=0
for i in range(size(vet)):
	if vet[i]%2!=0:
		vet2[j]=vet2[j]+i
		j=j+1
print(vet2)