#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#18/08/2016

from numpy import *

vetor = array(eval(input("Temperaturas: ")))

i = 0
j = 0
aceito = -100

while(i < size(vetor)):
	if(vetor[i] >= aceito): 
		j = j + 1
	i = i + 1

vetorR= array(zeros(j, dtype = float))

i=0
j =0
while(i < size(vetor)):
	if(vetor[i] >= aceito):
		vetorR[j] = vetor[i]
		j = j + 1
	i = i+1
print(vetorR)
