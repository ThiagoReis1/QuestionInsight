from numpy import *
vet = array(eval(input()))
r = 0
for i in range(size(vet)):
	if(vet[i]<5):
		r = r+1
print(r)
p = zeros(r,dtype=int)
for i in range(size(vet)):
	if(vet[i]<5):
		p[r]= p[r]+1
print(i)
		
print(p)