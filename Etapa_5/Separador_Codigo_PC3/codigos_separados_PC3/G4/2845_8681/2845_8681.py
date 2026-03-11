from numpy import *

ns = array(eval(input("Insira os numeros a serem substituidos: ")))
nu = zeros(size(ns), dtype = int)

for i in range(size(ns)):
	if i == 9:
		nu[i] = 0
	else:
		nu[i] = nu[i] + 1
		
print(nu)
	

