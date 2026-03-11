from numpy import*

vet = array(eval(input("Insira o vetor: ")))

a = 0

for i in range(size(vet)):
	if(vet[i] == 1):
		a = a + 1
z = zeros(a, dtype=int)

print(z)