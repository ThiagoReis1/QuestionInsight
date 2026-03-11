opcao=input("torta ou pastel? ").upper()
quantidade=int(input("quantos voce quer "))
capuccino=int(input("quantos voce quer "))

calculo1=quantidade*6 + capuccino*4.5
calculo2=quantidade*5 + capuccino*4.5

if opcao == "T":
	print(calculo1)
	
else:
	print(calculo2)