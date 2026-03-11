#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549

from numpy import *
distancia = array(eval(input("Digite a distancia:")))
recorde = 8.95
cont = 0
ac = 0
while(cont < size(distancia)):
	if(distancia[cont] < recorde):
		ac = ac + 1
	cont = cont + 1
print(recorde)
print(ac)