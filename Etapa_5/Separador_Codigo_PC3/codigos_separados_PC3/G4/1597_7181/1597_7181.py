from numpy import *

vet=array(eval(input("compras:  ")))
i=0
vc=0
while(i<size(vet)):
	if(vet[i]>80):
		vc=vc+vet[i]-5
	else:
		vc=vc+vet[i]
	i=i+1
print(vc)