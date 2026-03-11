from numpy import *

entrada = array(eval(input()), dtype=float)
n = len(entrada)
i = 0
numerador = 0
while(i < n ):
	numerador += entrada[i]**2
	i += 1
	
M = (numerador/n)**0.5
print(round(M,2))
