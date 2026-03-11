from numpy import*
from math import*

vet=array(eval(input()))

m=0

for i in range(size(vet)):
	m=m+log(vet[i]+1)
n=size(vet)
tot=exp(m/n)-1

print(round(tot,2))