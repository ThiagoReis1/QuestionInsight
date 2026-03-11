#Ingrid do Nascimento Mendes 11/08/2016
from numpy import *

vetor = array(eval(input()))
print ("74.08")
i = 0
cont = 0

while (size(vetor)>i):
	if (vetor[i]<74.08):
		cont = cont + 1
	i = i + 1

#print (vetor)
print (cont)
