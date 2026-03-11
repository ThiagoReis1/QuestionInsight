from numpy import *

vet = input("Digite a nacionalidade: ".split(','))
v =0
for i in range(len(vet)):
	if(vet[i]=="AR"):
		v[i] = v[i] + v
		
print(v)
