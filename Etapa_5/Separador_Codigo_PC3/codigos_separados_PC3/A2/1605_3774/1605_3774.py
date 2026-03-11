from numpy import*
alvo = array(eval(input("Digite os valores dos aneis acertados: ")))
size(alvo)
competidor = 200
i = 0

while(i < size(alvo)):
	if(alvo[i] == 1):
		competidor = competidor * 4
	elif(alvo[i] == 2):
		competidor = competidor * 2
	elif(alvo[i] == 3):
		competidor = competidor 
	else:
		competidor = competidor/2
	i += 1

print(round(competidor, 2))
		






