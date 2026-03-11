resultado = input("Resultado do time na competição: ")
vezes = input("Quantas vezes o time foi campeão: ")

if((resultado.upper() == "CAMPEAO") and (vezes == "06-vezes")):
	x = "CORINTHIANS"
	print(x)
elif((resultado.upper() == "CAMPEAO") and (vezes == "03-vezes")):
	x = "SANTOS"
	print(x)
elif((resultado.upper() == "VICE-CAMPEAO") and (vezes == "01-vez")):
	x = "FLAMENGO"
	print(x)
elif((resultado.upper() == "VICE-CAMPEAO") and (vezes == "06-vezes")):
	x = "INTERNACIONAL"
	print(x)
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")