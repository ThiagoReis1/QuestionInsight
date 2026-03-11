compra1 = float(input("Digitar compra 1: "))
compra2 = float(input("Digitar compra 2: "))
compra3 = float(input("Digitar compra 3: "))
compra4 = float(input("Digitar compra 4: "))
limite = float(input("Digitar limite: "))

valortotal = compra1 + compra2 + compra3 + compra4

if(valortotal <= limite):
	print("Sim")
else:
	print (round(valortotal,2))
	print("Nao")

