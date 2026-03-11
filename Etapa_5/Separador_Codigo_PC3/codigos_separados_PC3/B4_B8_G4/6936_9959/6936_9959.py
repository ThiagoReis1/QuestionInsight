x = float(input("valor total da compra: "))
y = input("opcao de pagamento: ").upper()

if y == "D":
	total = x - x * 0.13
elif y == "P":
	total = x - x * 0.13
elif y == "C":
	C = int(input("quantas vezes: "))
	if C == 2:
		total = x + x * 0.08
	else:
		total = x

print(round(total, 2))
			
		