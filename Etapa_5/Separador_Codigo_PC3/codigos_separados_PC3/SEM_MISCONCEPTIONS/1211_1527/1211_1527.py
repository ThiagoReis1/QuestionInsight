#Universidade Federal do Amazonas - UFAM
#Laís Amorim Reis - 21602327 
from numpy import *

pesos_levantamentos = eval(input("Informe os pesos: "))
recorde = 307 
i = 0
total = 0 

while(i<size(pesos_levantamentos)):
	if(pesos_levantamentos[i]>recorde):
		total = total + 1
	i = i + 1

print(recorde)
print(total)
		

