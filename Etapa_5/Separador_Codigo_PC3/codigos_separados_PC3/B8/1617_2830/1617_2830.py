from numpy import*

espada = array(eval(input()))
nivel = array(eval(input()))

i = 0 
dano = 0

while(i < size(espada)):
	if(espada[i] == "CENOURA"):
		dano = dano + 2*nivel[i] 
	elif(espada[i] == "FERRO"):
		dano = dano + 4*nivel[i] 	
	elif(espada[i] == "DWARVEN"):
		dano = dano + 8*nivel[i]
	elif(espada[i] == "ELVEN"):
		dano = dano + 11*nivel[i]	
	elif(espada[i] == "DAEDRIC"):
		dano = dano + 14*nivel[i]
	i = i + 1
print(dano)	