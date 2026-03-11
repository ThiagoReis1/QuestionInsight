from numpy import*
vet = array(eval(input("ALUNOS: ")))
n = 0 
for i in range(size(vet)):
	if vet[i] % 2 == 0:
		n = n + 1
print(n)
vet2 = zeros(n, dtype = int)
i = 0
for cont in range(0, size(vet)):
	if vet[cont] % 2 == 0:
		vet2[i] = cont
		i = i + 1
print(vet2)