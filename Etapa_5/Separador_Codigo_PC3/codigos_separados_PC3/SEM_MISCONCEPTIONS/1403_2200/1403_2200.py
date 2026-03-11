armadura = input("nome da armadura: ")
fator = int(input("fator de destreza: "))
malha = 15 * fator - 1
placas = 20 * fator - 18
if(armadura == "malha"):
	print(int(malha))
else:
	print(int(placas))