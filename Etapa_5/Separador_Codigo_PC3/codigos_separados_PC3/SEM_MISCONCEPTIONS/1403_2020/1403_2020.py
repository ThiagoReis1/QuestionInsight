armadura = input("nome da armadura: ")
fator = int(input("fator de destreza: "))

if(armadura == "malha"):
	resistencia = 15 * fator - 1
else: 
	resistencia = 20 * fator - 18
print(resistencia)