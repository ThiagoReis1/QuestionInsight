
from math import *

vetor = array(eval(input("Digite aqui o vetor: "

while( i < size(vetor)):
	if(vetor[i] < 10):
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
	if(vetor[b] > 10):
		vetor1[a]=vetor1[a]+vetor[b]
	
		b=b+1
