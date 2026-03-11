from numpy import *

n=array(eval(input()))

c=0

for i in range (size(n)):
	if (n[i]%2==0):
		c=c+1	
print(c)

vet=zeros(c, dtype=int)
j=0
for i in range (size(n)):
	if (n[i]%2==0):
		vet[j]=i
		j=j+1
print(vet)