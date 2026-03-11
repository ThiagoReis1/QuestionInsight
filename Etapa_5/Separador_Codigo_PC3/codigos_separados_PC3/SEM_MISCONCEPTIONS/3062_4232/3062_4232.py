PO=float(input("Quantidade de pecas de ouro: "))
arma=input("Nome da arma: (ESPADA, MACHADO OU MARRETA):")
fator=int(input("Fator de sucesso: "))
if(fator>1 and fator<10):
	if (arma=="ESPADA"):
		if (PO>=100):
			print(fator*10)
		else:
			print("PO insuficiente")
	elif(arma=="MARRETA"):
		if(PO>=50 and PO<100):
			print(fator+5)
		else:
			print("PO insuficiente")
	elif(arma=="MACHADO"):
		if(PO>=30 and PO<=50):
			print(fator+3)
		else:
			print("PO insuficiente")
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
