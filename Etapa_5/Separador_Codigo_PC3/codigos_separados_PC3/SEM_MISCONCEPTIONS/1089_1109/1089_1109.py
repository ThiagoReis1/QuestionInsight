compra1 = float(input("Compra 1: "))
compra2 = float(input("Compra 2: "))
compra3 = float(input("Compra 3: "))
limite = float(input("Qual o Limite do seu cartao? "))

total = compra1 + compra2 + compra3

if (total <= limite):
	print(round(total, 2))
	print("Sim")
else:
	print(round(total, 2))
	print("Nao")