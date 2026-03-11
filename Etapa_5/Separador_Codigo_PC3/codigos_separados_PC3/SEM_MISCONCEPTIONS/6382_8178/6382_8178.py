from numpy import*

numeros = array(eval(input()), dtype=int)

for i in range(size(numeros)):
	if numeros[i] == 9:
		numeros[i] = 0
	else:
		numeros[i] = (numeros[i] + 1)**2
print(numeros)
