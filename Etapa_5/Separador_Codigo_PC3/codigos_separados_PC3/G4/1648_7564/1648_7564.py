from numpy import*
vet = array(eval(input("")))
r=0

for i in range (size(vet)):
	if(vet[i]<70):
		r=r+1
print(r)
v1 = zeros(r,dtype=int)
j=0
for i in range(size(vet)):
	if(vet[i]<70):
		v1[j]=i
		j=j+1
print(v1)
		
	