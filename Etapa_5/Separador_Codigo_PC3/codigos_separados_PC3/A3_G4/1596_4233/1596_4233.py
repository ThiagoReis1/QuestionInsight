from numpy import*
from numpy.linalg import*

vet = array(eval(input("")))

soma = 0

for i in range(size(vet)):
	vet[i] = vet[i] - min(vet)

a = size(min(shape(vet)))

tamanho = shape(vet)[0]

m = sum(vet)/(size(vet)-1)

print(round(m,2))