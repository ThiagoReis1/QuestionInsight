from numpy import *

n = array(eval(input("digite o numero de 0 a 9: ")))
cont = zeros(size(n),dtype=int)

for x in range(size(n)):
	if n[x] == 9:
		cont[x] = 0
	else:
		cont[x] = (n[x] + 1) ** 2
		
print(cont)