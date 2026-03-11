from numpy import *
codigo = array(eval(input()))
for i in range(size(codigo)):
	if codigo[i] == 9:
		codigo[i] = 0
	else:
		codigo[i] = (codigo[i] + 1)**2
print(codigo)