from numpy import *
codigo = array(eval(input('insira os numeros inteiros de 0 a 9: ')))
segredo = zeros(codigo, dtype = int)

for i in range(0, size(codigo)):
	if codigo[i] == 7:
		codigo[i] = 49
	else:
		codigo[i] = codigo[i] ** 2
print(codigo)