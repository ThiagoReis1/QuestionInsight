from numpy import *

valor = array(eval(input()))
for i in range(len(valor)):
	if valor[i] == 9:
		valor[i] = 0
	else:
		valor[i] = (valor[i] + 1)**3
print(valor)