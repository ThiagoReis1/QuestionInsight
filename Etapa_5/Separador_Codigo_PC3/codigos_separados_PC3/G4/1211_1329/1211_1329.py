from numpy import *
rm=307
peso=array(eval(input("")))
i=0
cont=0
while(i<size(peso)):
	if(peso[i]>rm):
		cont+=1
	i+=1
print(rm)
print(cont)