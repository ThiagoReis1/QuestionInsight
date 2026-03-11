from numpy import *

vet = input("vetor: ").split(',')

i = 0
vet_0 = zeros(size(vet), dtype = int)


p = 0
c = 0
m = 0
v = 0
a = 0


while i < size(vet):
	i = i + 1
	if vet[i] == "P":
		vet_0[0] = p + 1
	elif vet[i] == "C":
		vet_0[1] = c + 1
	elif vet[i] == "M":
		vet_0[1] = c + 1
	
		