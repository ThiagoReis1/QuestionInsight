#Matriz padronizada

from numpy import *

n = int(input("Matriz quadrada: "))
f = zeros((n,n), dtype = int)

for i in range(shape(f)[0]):
	for j in range(shape(f)[1]):
		if j >= i :	
			f[i,j] = 1
print(f)
		
