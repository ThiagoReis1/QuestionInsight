from numpy import *

vet = array(eval(input()))

i = 0
qtd = 0
while (i < size(vet)):
	if (vet[i] > 217 ):
		qtd = qtd + 1
	i = i + 1
		
print ("217")
print (qtd)