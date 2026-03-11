from numpy import*
vet=array(eval(input("")))
s=0
j=0

for i in range(size(vet)):
	if(vet[i]<=50):
		s=s+1
		v[i] = i
print(s)
cont=zeros(size(s),dtype=int)

for j in range(size(s)):
	if(vet[i]<=50):
		cont=cont[j]+vet[i]
	i=i+1
	j=j+1
print(cont)

	