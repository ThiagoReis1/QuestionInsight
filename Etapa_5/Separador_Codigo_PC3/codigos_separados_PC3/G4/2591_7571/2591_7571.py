from numpy import*
from math import *
vet=array(eval(input(" ")))
v=0
for i in range(1,size(vet)):
	if(vet[i]<0 and vet[0]<abs(vet[i])):
		print(i)	
		v=v+1
print(v)
	