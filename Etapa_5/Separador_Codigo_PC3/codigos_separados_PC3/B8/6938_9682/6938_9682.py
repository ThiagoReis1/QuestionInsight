compra = float(input("Digite o valor da compra: "))
codigo = str(input("Digite o codigo [D], [P] ou [C]: ")).upper()
if codigo == "D" or codigo == "P":
	total = compra - compra*(11/100)
	print(round(total, 2))
elif codigo == "C":
	cartao = int(input())
	if cartao == 1:
		total = compra
		print(round(total, 2))
	elif cartao == 2:
		total = compra + compra*(6/100)
		print(round(total, 2))