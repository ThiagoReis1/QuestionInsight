from numpy import*
vet = array(eval(input('vetor vias: ')))
c = vet[0]
cont = 0
for i in range(1, size(vet)):
	if vet[i] < c:
		print(i)
		cont += 1
print(cont)