compra1 = float(input("valor1"))
compra2 = float(input("valor2"))
compra3 = float(input("valor3"))
limite = float(input("limite"))
total = round((compra1 + compra2 + compra3),2)

if(total <= limite):
	print(total)
	print("Sim")
else:
	print(total)
	print("Nao")
	
