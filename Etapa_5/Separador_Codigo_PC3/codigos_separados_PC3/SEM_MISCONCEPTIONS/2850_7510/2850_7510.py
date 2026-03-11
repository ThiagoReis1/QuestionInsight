import numpy as np

entrada = np.array(eval(input()))
limite = 55
cont = 0
for i in range(len(entrada)):
	cont+=entrada[i]
	if cont > limite:
		cont = 0
		
print(cont)