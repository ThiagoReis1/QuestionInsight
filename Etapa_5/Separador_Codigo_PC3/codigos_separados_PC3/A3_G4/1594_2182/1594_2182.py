from numpy import *
vet = array(eval(input("M:")))
i = 0
j = 0
dano = 1
while( i < size(vet)):
	dano = +(vet[i]*j)
	j = j + 1

print(dano)


