resultado = input("Digite o resultado do time nessa competição:").upper()
vezes = input("Digite a quantidade de vezes que foi campeão: ").upper()
if(resultado == "CAMPEAO") and (vezes == "11-VEZES"):
	print("REAL MADRID")
elif(resultado == "CAMPEAO") and (vezes == "05-VEZES"):
	print("BARCELONA")
elif(resultado == "VICE-CAMPEAO") and (vezes == "01-VEZ"):
	print("CHELSEA")
elif(resultado == "VICE-CAMPEAO") and (vezes == "04-VEZES"):
	print("MILAN")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")
	