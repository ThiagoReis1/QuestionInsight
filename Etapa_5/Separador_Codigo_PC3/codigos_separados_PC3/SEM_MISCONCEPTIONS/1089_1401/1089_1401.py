compra1 = float(input("Digite o valor da compra 1: "))
compra2 = float(input("Digite o valor da compra 2: "))
compra3 = float(input("Digite o valor da compra 3: "))

limite_cartao = float(input("Digite o limite do cartão: "))

compra_total = (compra1 + compra2 + compra3)

if (compra_total <= limite_cartao):
	print(round(compra_total,2))
	print("Sim")
else:
	print(round(compra_total,2))
	print("Nao")
	