from numpy import*
vet = array(eval(input("alunos: ")))
npar = 0
for i in range(size(vet)):
	if vet[i] % 2 == 0:
		npar = npar + 1
print(npar)
vet2 = zeros(npar,dtype=int)
i = 0
for cont in range(0, size(vet)):
	if vet[cont] % 2 == 0:
		vet2[i] = cont
		i = i + 1
print(vet2)
