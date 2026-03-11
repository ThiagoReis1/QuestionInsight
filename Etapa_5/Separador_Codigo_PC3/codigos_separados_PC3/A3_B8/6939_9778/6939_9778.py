subtotal = float(input("valor total da compra: "))
cod = input("('D') dinheiro; ('P') pix; ('C') cartao: "). upper()

total = subtotal

if cod == "D" or cod == "P":
	total = subtotal - subtotal * (19/100)
elif cod == "C":
	parcelas = int(input("qnts parcelas? (1) ou (2): "))
	if parcelas == 2:
		total= subtotal + subtotal * (9/100)
print(round(total, 2))