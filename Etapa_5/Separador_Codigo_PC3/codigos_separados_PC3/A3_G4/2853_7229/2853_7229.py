from numpy import *

v=array(eval(input()))

vet=zeros(v,dtype=int)
soma=0


a=0
for i in range(size(v)):
	if(v[i]==10):
		soma=soma*10
	soma=soma+v[i]
print(soma)