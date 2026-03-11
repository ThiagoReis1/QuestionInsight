from numpy import *

vet = input("paises: ").split(',')

p = zeros(5, dtype=int)

for i in range(size(vet)):
	if(vet[i].upper() == "CHN"):
		p[0] = p[0] + 1
	elif(vet[i].upper() == "JPN"):
		p[1] = p[1] + 1
	elif(vet[i].upper() == "KOR"):
		p[2] = p[2] + 1
	elif(vet[i].upper() == "MGL"):
		p[3] = p[3] + 1
	elif(vet[i].upper() == "THA"):
		p[4] = p[4] + 1
print(max(p))
print(p)