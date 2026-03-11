import numpy as np
espada = eval(input())
nivel = np.array(eval(input()),dtype = np.int)

count = 0
saida = 0
while (count<len(espada)):
	dano = 0
	if (espada[count] == 'CENOURA'):
		dano = nivel[count]*2
	elif(espada[count] == "FERRO"):
		dano = nivel[count]*4
	elif(espada[count] == "DWARVEN"):
		dano = nivel[count]*8
	elif(espada[count] == "ELVEN"):
		dano = nivel[count]*11
	else:
		dano = nivel[count]*14
		
	saida = saida + dano
	count = count + 1
print(saida)