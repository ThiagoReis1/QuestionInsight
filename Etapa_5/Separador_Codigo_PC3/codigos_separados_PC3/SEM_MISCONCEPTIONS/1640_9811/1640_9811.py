from numpy import *

clas = array(eval(input(":")))
impar = 0

for i in range(size(clas)):
	if clas[i] %2 != 0:
		impar += 1
		
quant = zeros(impar, dtype=int)
print(impar)
indice = 0

for i in range(size(clas)):
	if clas[i] % 2 != 0:
		quant[indice] = i
		indice += 1
		
print(quant)