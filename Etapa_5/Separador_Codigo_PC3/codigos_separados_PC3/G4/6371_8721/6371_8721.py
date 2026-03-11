from numpy import*

vet = array(eval(input("Digite o vetor: ")))
vet2 = zeros(size(vet), dtype = int)

for x in range(0,size(vet)):
	if vet[x] == 0:
		vet2[x] = 9**2
	else:
		vet2[x] = (vet[x]-1) ** 2
print(vet2)