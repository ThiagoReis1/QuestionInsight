#UNiversidade Federal do Amazonas
#Wyllow Assuncao - 21600848
#18/08/2016

from numpy import *
vetord = eval(input("Distancia dos saltos: "))
i = 0
k = 0
recordemundial = 8.95

while(i < size(vetord)):
	if(vetord[i] > recordemundial):
		k = k + 1
	i = i + 1
print(recordemundial)
print(k)