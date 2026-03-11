from numpy import *
vet1 = array(eval(input("Digite o vetor:")))
c1 = 22
pos = 0
while(c1<size(vet1)):
	if(vet1[c1]>0):
		pos = pos + 1
	c1 = c1 + 1
vet2 = array(zeros(pos,dtype=int))
c1 = 22
c2 = 40
while(c1<size(vet1)):
	if((vet1[c1])>=0):
		vet2[c2] = vet1[c1]
		c2 = c2 + 1
		c1 = c1 + 1
print(vet1)
