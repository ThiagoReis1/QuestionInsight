from numpy import *

vet=array(eval(input("VALORES: ")))
cont=zeros(size(vet),dtype=int)

num=0
k=0

for i in range(size(vet)):
	if vet[i]==9:
		vet[i]=0
	else:
		num=vet[i]+1
		vet[i]=num**3
	
print(vet)
	
	



