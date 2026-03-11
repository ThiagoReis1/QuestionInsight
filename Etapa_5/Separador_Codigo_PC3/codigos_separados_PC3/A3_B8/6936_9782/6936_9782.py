subtotal = float(input("Digite o valor da compra: "))
codigo = input("Selecione o codigo de pagamento (D) dinheiro (P) pix (C) cartao: ").upper()
total = subtotal 

if codigo == "D" or codigo == "P":
	total = subtotal - subtotal * .13
	print(round(total, 2))

elif codigo == "C":
	parcelamento = int(input("1 ou 2 vezes?: "))
	if parcelamento == 1:
		total = subtotal
		print(round(total, 2))
	else:
		total = subtotal + subtotal * .08
		print(round(total, 2))