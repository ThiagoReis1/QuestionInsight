from numpy import*

vet = array(eval(input("Digite o valores do saque: ")))

soma = 0

for i in range(size(vet)) :
	
	if vet[i] >= 2000 :
		
		soma = soma + 1

print(soma)

indice = 0
numero = zeros(soma, dtype = int)

for i in range(size(vet)) :
	
	if vet[i] >= 2000 :
		
		numero[indice] = i
		indice = indice + 1
		
print(numero)


