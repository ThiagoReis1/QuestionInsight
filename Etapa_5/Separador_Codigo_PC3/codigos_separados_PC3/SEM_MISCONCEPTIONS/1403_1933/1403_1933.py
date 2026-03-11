armadura = input("nome da armadura:")
destreza = int(input("fator de destreza:"))
malha = 15 * destreza - 1
placas = 20 * destreza - 18 
if(armadura == "malha"):
	print(malha)
else:
	print(placas)