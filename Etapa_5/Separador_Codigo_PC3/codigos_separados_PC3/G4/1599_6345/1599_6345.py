from numpy import *

vet = array(eval(input("custo dos itens: ")))

i = 0
s = 0

while (i<size(vet)):
	s = s + vet[i]
	
	if (vet[i]>80.0):
		s = s + 80 - 80 * 0.15
		
	i = i + 1
	
print (s)