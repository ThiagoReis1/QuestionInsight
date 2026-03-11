subtotal = float(input("valor total de compra"))
cod= input("(D)dinheiro;(P) pix; (C)cartao:").upper()
total= subtotal

if cod == "D" or cod == "P":
	total = subtotal - subtotal * (18/100)
elif cod == "C":
	parcelas = int(input("quantas parcelas (1) ou (2)"))
	if parcelas == 1: 
		total = subtotal 
	if parcelas == 2:
		total = subtotal + subtotal * (7/100)
print(round(total,2))



