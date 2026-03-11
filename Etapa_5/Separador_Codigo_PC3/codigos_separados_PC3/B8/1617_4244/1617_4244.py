from numpy import*

espada = input("Tipo de espada: ")
nivel = array(eval(input("Nivel: ")))

dano = 0
formula = dano*nivel

while(size(nivel)>0):
	if(espada == "CENOURA"):
		dano = dano + 2
		print(formula)
	elif(espada == "FERRO"):
		dano = dano + 4
		print(formula)
	elif(espada == "DWARVEN"):
		dano = dano + 8
		print(formula)
	elif(espada == "ELVEN"):
		dano = dano + 11
		print(formula)
	elif(espada == "DAERDRIC"):
		dano = dano + 14
		print(formula)
