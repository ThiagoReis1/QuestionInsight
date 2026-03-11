from numpy import array, size
entrada = array(eval(input()))
for i in range(size(entrada)):
	if(entrada[i] != 0):
		entrada[i] = (entrada[i]-1)**3
	else:
		entrada[i] = 9 ** 3
print(entrada)