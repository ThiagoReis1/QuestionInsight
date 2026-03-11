from numpy import *
vet=array(eval(input("vias:")))
qtdvia=0
for i in range(size(vet)):
	if (vet[0]>vet[i]):
		qtdvia=qtdvia+1
		print(i)
print(qtdvia)