from numpy import *

codigo = array(eval(input("Insira o seu codigo: ")))
codigo_novo = zeros(size(codigo), dtype=int)

for i in range(size(codigo)):
	if codigo[i] == 0:
		codigo_novo[i] = 9 ** 2
	else:
		codigo_novo[i] = (codigo [i]) ** 2
print(codigo_novo)