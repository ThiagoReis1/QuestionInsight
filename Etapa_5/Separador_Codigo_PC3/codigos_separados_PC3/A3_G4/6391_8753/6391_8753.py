from numpy import*
vet = array(eval(input("vetor: ")))
verb = zeros(size(vet), dtype = int)
k = 0
numi = size(vet)

for i in vet:
	if (i != 0):
		verb[k] = (vet[k] - 1) ** 3
	else:
		verb[k] = 9 ** 3
	k += 1
print(verb)