from numpy import *
vet = array(eval(input("vetor: ")))
i = 0
npar=0


for i in range(size(vet)):
	if (vet[i] >= 70):
		npar = npar + 1
print(npar)

cont = zeros(npar, dtype=int)
d = 0
for i in range(size(vet)):
	if (vet[i] >= 70):
		cont[d] = i
		d = d + 1
print(cont)