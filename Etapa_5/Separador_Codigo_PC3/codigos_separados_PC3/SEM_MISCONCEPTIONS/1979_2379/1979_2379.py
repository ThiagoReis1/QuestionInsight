resultado = input()
vezes = input()

if(resultado == "Campeao") and (vezes == "05-vezes"):
	print("BRASIL")
elif(resultado == "Campeao") and (vezes == "04-vezes"):
	print("ITALIA")
elif(resultado == "Vice-Campeao") and (vezes == "04-vezes"):
	print("ALEMANHA")
elif(resultado == "Vice-Campeao") and (vezes == "03-vezes"):
	print("ARGENTINA")
else:
	print("SELECAO NAO IDENTIFICADA")