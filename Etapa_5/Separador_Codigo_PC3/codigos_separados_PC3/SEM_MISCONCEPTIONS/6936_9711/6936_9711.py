compra = float(input("digite o valor da compra: "))
codpag = input("digite o codigo do pagamento: ")
if codpag == "D" or codpag == "P":
	valor = compra* 0.13
elif codpag == "C":
	valor = compra
elif codpag 