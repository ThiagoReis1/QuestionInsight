from numpy import *

vet=array(eval(input()))
reprov=0
for i in range(size(vet)):
	if(vet[i]<70):
		reprov=reprov+1
		
vetreprov=zeros(reprov,dtype=int)
cont=0
for i in range(size(vet)):
	if(vet[i]<70):
		vetreprov[cont]=i
		cont=cont+1
print(reprov)
print(vetreprov)