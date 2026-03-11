from numpy import *
a=eval(input())
i=0
cont=0
vet = zeros(size(a),dtype=float)
while (i<size(a)):
	if(a[i]<-60 or a[i]>60):
		vet[i] = a[i]
		cont= cont+1
	i = i+1
vet2 = (zeros(cont,dtype=float))
y=0
z=0
while (y<size(vet)):
	if(-60<=vet[y]<=-60):
		vet2[z]=vet[y]
		z = z+1
	y = y+1
print (vet2)
