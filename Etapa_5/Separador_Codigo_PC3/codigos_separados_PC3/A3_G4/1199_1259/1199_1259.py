#Julia Caroline
#11 de Agosto de 2016
#Avaliacao 05 Ex2

from numpy import*
#le o vetor
vet = array(eval(input("temperaturas: ")), dtype = float)
#variaveis de controle
i = 0
j = 0
k = 0
cont = 0
achou = False
#encontra os elementos
while(i < size(vet)):
	if((vet[i] > 10.0) or (vet[i]) < 40.0 ):
		cont = cont + 1
	i = i + 1
#vetor resultante
vet2 = array(cont, dtype = float)

#elementos do vetor resultante
while(j < size(vet)):
	if((vet[j] > 10.0) or (vet[j]) < 40.0 ):
		achou = True
	if(achou == True and k < size(vet2)):
		vet2[k] = vet[j]
		k = k + 1
	j = j + 1
print(round(vet2, 1))
		
		

