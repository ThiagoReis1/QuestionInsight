from numpy import*
v=array(eval(input("Digite aqui o vetor")))
vet=zeros(2,dtype=int)
a=min(v)
b=max(v)
c=0.7*a+0.3*b
d=0.4*a+0.6*b
for i in range(size(v)):
	if((v[i]>a or v[i]==a) and v[i]<c):
	   vet[0]=vet[0]+1
	elif((v[i]>c or v[i]==c) and v[i]<d):
		vet[1]=vet[1]+1
print(vet)
     