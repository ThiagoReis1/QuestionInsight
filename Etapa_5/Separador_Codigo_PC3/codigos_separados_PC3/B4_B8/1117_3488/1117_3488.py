p = float(input("preco: "))
d = int(input("dia: "))
j = input("S/N: ")
preco = p + 20
preco1 = p * 25/100 

fav = preco - preco1

if (p >= 0) and (d <= 7) and (j == "S" or j == "N"):
	if p >= 0 and d == 1 and j == "S":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",preco)
	
	elif p >= 0 and d == 1 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",p)
	
	elif p >= 0 and d == 2 and j == "S":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(fav, 2))
	
	elif p >= 0 and d == 2 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(preco1, 2))
	
	elif p >= 0 and d == 3 and j == "S": 
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(fav, 2))
	
	elif p >= 0 and d == 3 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(preco1, 2))
	
	elif p >= 0 and d == 4 and j == "S":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",preco)
	
	elif p >= 0 and d == 4 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",p)
	
	elif p >= 0 and d == 5 and j == "S": 
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(fav, 2))
	
	elif p >= 0 and d == 5 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",round(preco1, 2))
	
	elif p >= 0 and d == 6 and j == "S":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",preco)
	
	elif p >= 0 and d == 6 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",p)
	
	elif p >= 0 and d == 7 and j == "S":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",preco)
	
	elif p >= 0 and d == 7 and j == "N":
		print("Entradas:",p,",",d,",",j)
		print("Valor a pagar: R$",p)
	
else:
	print("Entradas:",p,",",d,",",j)
	print("Dados invalidos")