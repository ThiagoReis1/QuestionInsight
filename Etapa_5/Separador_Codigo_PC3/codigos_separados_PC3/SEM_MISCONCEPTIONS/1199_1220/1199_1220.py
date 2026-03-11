from numpy import *
vet=array(eval(input("Informe as temepraturas: ")))
x=10
i=0
c=0
while(i<size(vet)):
	if(vet[i]<x):
		c=c+1
	i=i+1
vet2=array(c, dtype = int)
y=40
j=0
g=0
while(j<size(vet2)):
	if(vet2[j]>y):
	     vet2(g)=v(j)
	g=g+1
j=j+1
print(vet2)