from numpy import*
from math import*
p=eval(input("Digite:"))
vetor1= array(eval(input("Digite:")))
vetor2= array(eval(input("Digite:")))
soma=0
cont=zeros(size(vetor1))
for i in range(size(vetor1)):
	cont[i]= vetor1[i]+vetor2[i]
	t=p/p-1
	q=abs((cont[i]**t)/t)
print(round(q,5))