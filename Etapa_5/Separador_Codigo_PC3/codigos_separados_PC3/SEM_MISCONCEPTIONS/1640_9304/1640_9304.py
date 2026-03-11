from numpy import *

turmas = eval(input("Vetor turmas: "))

for i in range(size(turmas),-1,-1):
	a = 0
	size = size(turmas)
	if(turmas[size] % 2 != 0):
		a = a + 1
		size = size - 1
	else:
		size = size - 1 
print(a)