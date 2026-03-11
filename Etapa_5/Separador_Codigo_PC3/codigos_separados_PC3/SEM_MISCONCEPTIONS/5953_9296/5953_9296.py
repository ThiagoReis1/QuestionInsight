ped = input("Qual o pedido (L ou P)? ")
quant = int(input("Qual a quantidade de lanches ou pratos executivos? "))
refri = int(input("Qual a quantidade de refrigerants? "))
precl = (quant * 6.00) + (refri * 3.00)
precp = (quant * 13.50) + (refri * 3.00)
if (ped == "L"):
	 print(round(precl, 2))
else:
	 print(round(precp, 2))