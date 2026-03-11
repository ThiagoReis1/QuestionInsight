# Talita Passos
# 11 de Agosto de 2016
# Avaliacao 5 - Ex 01

from numpy import *

#indice do v1
i = 0
#numero de atletas/variavel acumuladora
j = 0


v1 = array(eval(input("Digite as distâncias: ")))

recorde = 8.95
print(recorde)

while(i < size(v1)):
	if(v1[i] > recorde):
		j = j + 1
	i = i + 1 
	
print(j)