from numpy import *
peso = eval(input())
i=0
k=0
recorde=307
tam = size(peso)
while (i < tam):
	if(peso[i] > recorde):
		k=k+1
	i=i+1
print(recorde)
print(k)
		
		