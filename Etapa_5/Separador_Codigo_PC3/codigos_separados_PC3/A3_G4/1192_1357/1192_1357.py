from numpy import*
a= float(input())
x=0
cont=0
vet=zeros(size(a),dtype=int)
while(x<size(a)):
	if(a[x]>=0):
		vet[x]=a[x]
		cot+=1
	x+=1
vet2=(zeros(count,dtype=int))
y=0
z=0
while(y<size(vet)):
	if(vet[y]>=0):
		vet2[z]=vet[y]
		z+=1
	y+=1
print(vet2)	