from numpy import *

entrada = array(eval(input()))

for i in range(len(entrada)):
	if(entrada[i] == 0):
		entrada[i] = 9**3
	else:
		entrada[i] = (entrada[i]-1)**3
		
print(entrada)