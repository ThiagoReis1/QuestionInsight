from numpy import*


vet = array(eval(input()))

i = 0

j = 0

reprov = 0



for elemento in vet:

	if(elemento < 5):

		reprov = reprov + 1


vat = zeros(reprov, dtype=int)


for elemento in vet:

	if(elemento < 5):

		vat[j] = i

		j = j +1

	i = i +1

print(reprov)

	

print(vat)