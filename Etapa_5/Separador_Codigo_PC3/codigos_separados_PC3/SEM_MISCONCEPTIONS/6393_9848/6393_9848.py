from numpy import *

codigo = array(eval(input('insira o codigo: ')))
codigo_new = zeros(size(codigo), dtype = int)

for i in range(size(codigo)):
	if codigo[i] == 9:
		codigo_new [i] == 0**3
	else:
		codigo_new[i] = (codigo[i] + 1) **3
		
print(codigo_new)
	