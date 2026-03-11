from numpy import *

v=array(eval(input()))

par=0
for i in range(size(v)):
	if(v[i]%2==0):
		par=par + 1
		


vet=zeros(size(v)-par,dtype=int)
j=0
for i in range(size(v)):
	if(v[i]%2==1):
		vet[j]=v[i]
		j=j+1
		
print(vet)

#for i in range(size(vet)):
	