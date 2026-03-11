from numpy import *
vet = array(eval(input("registro de vel: ")))
inf = 0

for i in range(1, size(vet)):
	if (vet[i] >= 1.5*vet[0]):
		inf = inf + 1
		print(i)
print(inf)