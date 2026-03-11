resultado = input("digite o resultado do time nessa competiçao: ").upper()
vezes = input("digite quantas vezes a selecao alcancou o resultado: ").upper()
if ((resultado == "CAMPEAO") and (vezes == "05-VEZES")):
	print("BRASIL")
elif ((resultado == "CAMPEAO") and (vezes == "04-VEZES")):
	print("ITALIA")
elif (("VICE-CAMPEAO") and (vezes == "04-VEZES")):
	print("ALEMANHA")
elif (("VICE-CAMPEAO") and (vezes == "03-VEZES")):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")
	
