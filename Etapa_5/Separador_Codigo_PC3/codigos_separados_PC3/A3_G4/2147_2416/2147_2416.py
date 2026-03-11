from numpy import*
vet=array(eval(input("")))
a=zeros(11,dtype=int)
while size(vet)<11:
	a=0
for i in range(size(vet)):
	
	if vet[i]%2==0:
		a[0]+=1
	if vet[i]%2==0:
		a[1]+=1		
	if vet[i]%2==0:
		a[2]+=1	
	if vet[i]%2==0:
		a[3]+=1	
print(a)		
		