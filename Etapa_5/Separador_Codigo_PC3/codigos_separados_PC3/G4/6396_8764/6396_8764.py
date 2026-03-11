from numpy import*

vet = array(eval(input("Digite o vetor: ")))
#novo = zeros(vet, dtype = int)

for i in range(size(vet)):
	vet[i] = vet[i] * 2
print(vet)