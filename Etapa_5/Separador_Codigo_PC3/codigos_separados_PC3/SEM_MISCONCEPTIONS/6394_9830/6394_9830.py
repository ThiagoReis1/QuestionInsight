from numpy import *
codigo = array(eval(input("")))
codigo_new = zeros(size(codigo), dtype=int)

for i in range(size(codigo)):
	if codigo[i] == 0:
		codigo_new[i] = 1
	elif codigo[i] == 9:
		codigo_new[i] = 0
	else:
		codigo_new[i] = codigo[i] + 1
	
print(codigo_new)