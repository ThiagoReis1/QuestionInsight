from numpy import *
vet = array(eval(input()))

i= 0
cont = 0

while i < size (vet):
	if vet[i] == 1:
		cont= cont + 80
	elif vet[i] == 2:
		cont= cont + 40
	elif vet[i] == 3:
		cont= cont + 20
	elif vet[i] == 4:
		cont = cont + 10
	i +=1
print(cont)
		