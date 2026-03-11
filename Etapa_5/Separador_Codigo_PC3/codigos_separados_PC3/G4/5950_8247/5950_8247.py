tipo = input("Digite T para torta e P para pastel")
quan = int(input("Insira a quantidade: "))
cap = int(input("Insira a quantidade de capuccinos: "))
if tipo == "T":
	total = quan*6 + 4.5*cap
	print(round(total, 2))
else:
	total = quan*5 + 4.5*cap
	print(round(total, 2))