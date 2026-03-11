#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#18/08/2016

from numpy import *

vetor = array(eval(input("Distancias: ")))

i = 0
cont_abaixo = 0

recorde = 8.95

while(i < size(vetor)):
	if(vetor[i] < recorde):
		cont_abaixo = cont_abaixo + 1
	i = i + 1
		
print(recorde)
print(cont_abaixo)
