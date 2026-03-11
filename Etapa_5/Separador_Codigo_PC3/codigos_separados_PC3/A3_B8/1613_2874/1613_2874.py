from numpy import *

atividade = array(eval(input("atividade: ")))
tempo = array(eval(input("Duração: ")))

calorias = zeros(size(atividade), )
i = 0
gasto = 0

while(i < size(atividade)):
	if(atividade[i] == "ALONGAMENTO"):
		gasto = 3.0
	elif(atividade[i] == "CORRIDA"):
		gasto = 10.3
	elif(atividade[i] == "DANCA"):
		gasto = 6.7
	elif(atividade[i] == "ESCALADA"):
		gasto = 9.7
	elif(atividade[i] == "HIDROGINASTICA"):
		gasto = 5.0
	
	calorias[i] = tempo[i] * gasto
	i += 1
print(round(sum(calorias),2))
