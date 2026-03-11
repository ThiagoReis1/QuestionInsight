from numpy import *

codigo = array(eval(input()))
codigo_novo = zeros(size(codigo),dtype=int)

for i in range(size(codigo)):
	if codigo [i] == 9:
		codigo_novo[i] = 0**3
	else:
		codigo_novo[i] = (codigo[i] +1)**3
print(codigo_novo)