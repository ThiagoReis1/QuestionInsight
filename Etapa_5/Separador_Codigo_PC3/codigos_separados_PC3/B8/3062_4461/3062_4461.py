ouro = float(input("ouro: "))
arma = input("arma: ")
sucesso = int(input("fator de sucesso: "))

if(arma == 'ESPADA' and ouro >= 100):
	print(sucesso * 10)
elif(arma == 'MACHADO'and ouro >= 30):
	print(sucesso + 3)
elif(arma == 'MARRETA'and ouro >= 50):
	print(sucesso + 5)
elif(ouro < 30):
	print("PO insuficiente")
elif(sucesso > 10 or arma != 'ESPADA' or arma != 'MACHADO' or arma != 'MARRETA'):
	print("Entrada invalida")