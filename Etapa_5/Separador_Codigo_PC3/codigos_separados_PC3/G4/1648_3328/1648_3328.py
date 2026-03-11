from numpy import *

vet=array(eval(input("valor: ")))
rp=0

for i in range(size(vet)):
	if(vet[i]<70):
		rp=rp+1
print(rp)
	
vet2=zeros(rp, dtype=int)

j=0
for i in range(size(vet)):
	if(vet[i]<70):
		vet2[j]=i
		j=j+1
print(vet2)