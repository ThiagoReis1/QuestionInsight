from numpy import *

vet = array(eval(input("Informe o vetor: ")))

i = 0
qtd = 0
while (i < size(vet)):
	if (vet[i] > 78.08):
		qtd = qtd + 1
	i = i + 1
print ("78.08")
print (qtd)