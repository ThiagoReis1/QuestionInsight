import numpy as np

aux = np.array(eval(input()))
count = 0

while(count < len(aux)):
	if(aux[count] < 9):
		aux[count] = (aux[count] + 1)**2
	else:
		aux[count] = 0
	count += 1
print(aux)