from numpy import *

cdg = array(eval(input("Digite o codigo a ser substituido: ")))

cont = zeros(size(cdg), dtype = int)

for i in range (size(cdg)):
	if (cdg[i] == 0):
		cont[i] = 0
		
	else:
		cont[i] = cdg[i] * 2
		
print(cont)