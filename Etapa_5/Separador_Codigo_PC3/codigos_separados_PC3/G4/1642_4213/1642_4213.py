from numpy import *
a=array(eval(input("Turmas:")))
b=size(a)
tur=0
for i in range(b):
	if a[i]%5==0:
		tur=tur+1
vet=zeros(tur, dtype=int)
e=0
for i in range(b):
	if a[i]%5==0:
		vet[e]=i
		e=e+1
print(tur)
print(vet)