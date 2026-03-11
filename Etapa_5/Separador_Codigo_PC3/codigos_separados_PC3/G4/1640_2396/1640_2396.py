from numpy import *

v=array(eval(input()))

cont=0
for i in range(size(v)):
	if(v[i]%2==1):
		cont=cont + 1
		
vet=zeros(cont,dtype=int)

print(cont)

j=0

for i in range(size(v)):
	if(v[i]%2==1):
		vet[j]=i
		j=j+1
		
print(vet)

#for i in range(size(vet)):
	