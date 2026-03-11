from numpy import*

numeros = array(eval(input("Digite um vetor de numeros: ")))

total = 0

for i in range(size(numeros)):
	if total + numeros[i] < 55:
		total = total + numeros[i]
	else:
		total = 0
		
print(total)