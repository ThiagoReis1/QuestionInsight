from numpy import * 
espada = array(input(": "))
combate = array(eval(input(": ")))
i = 0
dano = 0
while(i < size(combate)):
	if(espada[i] == "CENOURA"):
		dano = dano + 2 * combate[i]
	elif(espada[i] == "FERRO"):
		dano = dano + 4 * combate[i]
	elif(espada[i] == "DWARVEN"):
		dano = dano + 8 * combate[i]
	elif(espada[i] == "ELVEN"):
		dano = dano + 11 * combate[i]
	else:
		dano = dano + 14 * combate[i]
	i = i + 1					
print(dano)