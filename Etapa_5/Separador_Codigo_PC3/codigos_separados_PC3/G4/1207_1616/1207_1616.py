from numpy import *

vet = array(eval(input("Informe o vetor: ")))

i = 0
qtd = 0
while (i < size(vet)):
	if (vet[i] > 98.48 ):
		qtd = qtd + 1
	i = i + 1
		
print ("98.48")
print (qtd)