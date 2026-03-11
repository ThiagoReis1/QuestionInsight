from math import *
nome = input("Digite se é Campeao ou Vice-Campeao:")
vezes = input("Digite 05-vezes 04-vezes ou 03-vezes:")
if(nome.upper() == "CAMPEAO"):
	if(vezes.upper() == "05-VEZES"):
		print("BRASIL")
	elif(vezes.upper() == "04-VEZES"):
		print("ITALIA")
	else:
		print("SELECAO NAO IDENTIFICADA")
elif(nome.upper() == "VICE-CAMPEAO"):
	if(vezes.upper() == "04-VEZES"):
		print("ALEMANHA")
	elif(vezes.upper() == "03-VEZES"):
		print("ARGENTINA")
	else:
		print("SELECAO NAO IDENTIFICADA")
else:
	print("SELECAO NAO IDENTIFICADA")