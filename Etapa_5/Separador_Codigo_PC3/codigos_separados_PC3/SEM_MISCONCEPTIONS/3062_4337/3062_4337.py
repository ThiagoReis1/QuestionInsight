pecas = int(input())
arma = input()
sucesso = int(input())

if(1 <= sucesso <= 10 and arma.upper() == "MACHADO" or arma.upper() == "MARRETA" or arma.upper() == "ESPADA"):
	if(pecas >= 30 and arma.upper() == "MACHADO"):
		print(sucesso + 3)
	elif(pecas >= 50 and arma.upper() == "MARRETA"):
		print(sucesso + 5)
	elif(pecas >= 100 and arma.upper() == "ESPADA"):
		print(sucesso * 10)
	else:
		print("PO insuficiente")
else:
	print("Entrada invalida")