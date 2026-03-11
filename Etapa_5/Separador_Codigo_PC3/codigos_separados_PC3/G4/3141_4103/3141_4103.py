from numpy import *

n = array(eval(input("Entrada do vetor: ")))

i = 0
somat = 0
while (i < size(n)):
	if (n[i] >= 0):
		x = n[i]**(1/6)
		i = i + 1
		somat = somat + x 
M = (somat/size(n))**6
print(round(M, 2))