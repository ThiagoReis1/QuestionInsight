from numpy import*
vet=array(eval(input()))
for i in range(size(vet)):
	m= ((vet[i]**1/6)+(vet[i+1]**1/6)+size(vet-1)**1/6)**6
	print(m)