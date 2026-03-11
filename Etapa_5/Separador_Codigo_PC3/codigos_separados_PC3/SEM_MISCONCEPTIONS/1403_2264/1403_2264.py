nome_da_armadura = input("digite o nome da armadura(malha ou placas:)")
fator_de_destreza = int(input("valor entre 1 e 8"))

if(nome_da_armadura.lower() == "malha"):
	resistencia = 15 * fator_de_destreza - 1
	print(int(resistencia))
else:
	resistencia = 20 * fator_de_destreza - 18
	print(int(resistencia))