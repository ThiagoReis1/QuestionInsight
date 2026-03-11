from numpy import*

turmas = eval(input("Digite um valor:"))
soma = 0


for i in turmas:
	if i%3 == 0:
		soma = soma + 1
print(soma)

vet = []
indice = zeros(size(vet), dtype=int)

for i in range(size(turmas)):
	if turmas[i]%3 == 0:
		indice = i
print(indice)

	
		

		 