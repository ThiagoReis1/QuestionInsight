from numpy import*
from math import*
v=array(eval(input("digite o vetor: ")))
t=0
z=0
for x in v:
	if(x % 3 == 0):
		t=t+1
print(t)
vet=zeros(t,dtype=int)

for i in range(size(v)):
	if(v[i]%3==0):
		vet[z]=vet[i]
		z=z+1
print(vet)



		

		

