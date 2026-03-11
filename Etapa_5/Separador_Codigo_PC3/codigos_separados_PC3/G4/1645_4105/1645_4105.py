from numpy import*
vet=array(eval(input()))
i=0
r=0
while(i<size(vet)):
	if(vet[i]>=2000):
		r=r+1
	i=i+1
print(r)
x=zeros(r,dtype=int)
a=0
for i in range(size(vet)):
	if(vet[i]>=2000):
		x[a]=i
		a=a+1
print(x)
	