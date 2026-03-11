from numpy import *
vet = array(eval(input("")))
cont = 0
c=0
for i in range(0,size(vet)):
	if(vet[i] > 0.5*vet[0]+vet[0]):
		cont = cont + 1
	else:
		c=c+1
	print(c)
	print(cont)
