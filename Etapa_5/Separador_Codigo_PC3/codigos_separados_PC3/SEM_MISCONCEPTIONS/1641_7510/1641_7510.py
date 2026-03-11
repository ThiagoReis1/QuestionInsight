import numpy as np
entrada = np.array(eval(input()))


indice = [] 
cont = 0
for i in range(len(entrada)):
	if entrada[i] % 3 == 0:
		indice.append(i)
		cont+=1
print(cont)
print(np.array(indice))
	