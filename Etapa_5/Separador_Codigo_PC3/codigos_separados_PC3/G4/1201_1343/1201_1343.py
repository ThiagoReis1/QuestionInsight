from numpy import*
a=eval(input())
x=0
cont=0
vet=zeros(size(a),dtype=float)
while(x<size(a)):
	if(a[x]>0 and a[x]<40):
		vet[x]=a[x]	
		cont+=1
	x+=1
vet2=(zeros(cont,dtype=float))
y=0
z=0
while(y<size(vet)):
	if(vet[y]!=0):
		vet2[z]=vet[y]	
		z+=1
	y+=1
print(vet2)	
