from numpy import*

numeros = array(eval(input('Insira sua senha: ')))
numero2 = zeros(size(numeros), dtype = int)

for i in range (size(numeros)):
	if numeros[i] == 9:
		numeros[i] = 0 
	else:
		numeros [i] = (numeros[i] + 1) ** 3
		
print(numeros)