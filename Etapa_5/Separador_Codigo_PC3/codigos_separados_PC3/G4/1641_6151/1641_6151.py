from numpy import *

vet= array(eval(input('digite a lista de turmas: ')))
trio= 0

for i in vet:
	if (i%3==0):
		trio= trio+1
		
vetfinal= zeros(trio, dtype=int)
a= 0
ind= 0

for j in vet:
	if (j%3==0):
		vetfinal[a]= ind
		a= a+1
		ind= ind+1
	else:
		ind= ind+1
		
print(trio)
print(vetfinal)