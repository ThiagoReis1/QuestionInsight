from numpy import *

vet=array(eval(input()))

i=0
acum=0
while i< size(vet):
	acum=acum+vet[i]*(i+1)
	i=i+1
	
print(acum)