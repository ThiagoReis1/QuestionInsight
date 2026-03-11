from numpy import *

icomp = array(eval(input()))

cont = 0

for i in range(size(icomp)):
	if icomp[i] % 2 != 0:
		cont += 1
print(cont)
j = 0
ice = zeros(cont, dtype = int)
for i in range(size(icomp)):
	if icomp[i] % 2 != 0:
		ice[j] = i
		j = j + 1
print(ice)
		
	
		

	