from numpy import*
from math import *

vetor=array(eval(input("Digite aqui o vetor:")))

i=0
k=0
while(i<size(vetor)):
	if(vetor[i]!=abs(vetor[i])):
		k=k+1
		i=i+1
	else:
		i=i+1
p=size(vetor)
num=p-k
vetor1=zeros(num, dtype=float)
a=0
b=0
while(a<num):
	if(vetor[b]==abs(vetor[b])):
		vetor1[a]=vetor1[a]+vetor[b]
		b=b+1
		a=a+1
	else:
		b=b+1
print(vetor1)