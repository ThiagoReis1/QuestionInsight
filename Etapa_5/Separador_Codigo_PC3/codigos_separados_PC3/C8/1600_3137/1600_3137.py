from numpy import*
from numpy.linalg import*

compras = array(eval(input()))
i = 0 
t = 0
for i in range (compras[i]> 80):
	i = i + 1 
	t = t + 1	
	compras[i] = compras[i] - compras[i]*0.15  

print(sum(compras[i]))