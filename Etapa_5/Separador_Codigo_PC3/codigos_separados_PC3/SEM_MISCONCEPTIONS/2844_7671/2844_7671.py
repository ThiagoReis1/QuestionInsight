#Codigo
from numpy import *

cod = array(eval(input("digite o codigo: ")))

saida = zeros(size(cod), dtype=int)

for i in range(size(cod)):
	if(cod[i] != 0):
		saida[i] = cod[i] - 1
	else:
		saida[i] = 9
	
print(saida)
	