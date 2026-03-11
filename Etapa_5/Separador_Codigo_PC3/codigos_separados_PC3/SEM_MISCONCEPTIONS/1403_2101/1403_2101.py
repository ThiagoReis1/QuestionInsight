armadura = input("digite o nome da armadura: ")
fator = int (input("valor entre 1 e 8: "))

if armadura == "malha" :
	resistencia = 15 * fator - 1
	print (int(resistencia))
	
else :
	resistencia_2 = 20 * fator - 18
	print (int(resistencia_2))