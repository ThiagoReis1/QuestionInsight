compra1 = float(input("valor da compra 1: "))
compra2 = float(input("valor da compra 2: "))
compra3 = float(input("valor da compra 3: "))
compra4 = float(input("valor da compra 4: "))
limite = float(input("limite do cartao: "))
total = compra1 + compra2 + compra3 + compra4
print(round(total, 2))

if(total <= limite):
		print("Sim")
else:
	print("Nao")
	