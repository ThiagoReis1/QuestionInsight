Lanche = input("Bolo ou Croissant: ")
QtdBC = int(input("Quantidade de fatias de bolo ou croissant: "))
Capp = int(input("Quantidade de cappuccinos: "))

ValorB = 3.00
ValorC = 6.00
ValorCapp = 5.50

if Lanche == "B":
	valor_total = (QtdBC*ValorB) + (Capp*ValorCapp)
	print(valor_total)
else:
	valor_total = (QtdBC*ValorC) + (Capp*ValorCapp)
	print(valor_total)
	

	
	