from numpy import *

vet1 = array(eval(input("Digite o vetor:")))
t1 = 28
pos = 0

while(t1<size(vet1)):
	if((vet1[t1])>0):
		pos = pos + 1
	t1 = t1 + 1

vet2 = array(zeros(pos,dtype=int))
t1 = 28
t2 = 50

while(t1<size(vet1)):
	if((vet1[t1])>=0):
		vet2[t2] = vet1[t1]
		t2 = t2 + 1
	t1 = t1 + 1
print(vet1)