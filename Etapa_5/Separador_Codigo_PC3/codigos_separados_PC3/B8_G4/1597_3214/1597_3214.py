from numpy import *
vet=array(eval(input()))
for i in range(size(vet)):
	if vet[i]>80:
		x=sum(vet)-5
	elif i<=80:
		x=sum(vet)
print(round(x,2))		