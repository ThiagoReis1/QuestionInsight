valor = float(input("informe o valor da compra: "))
cod = input("informe a opcao de pagamento: ").upper()

if cod == "C":
	v = int(input("informe em quantas parcelas: "))
	if v == 1:
		desc = 0
		total = valor - (valor * desc)
		print(round(valor, 2))
	else:
		total = valor + (valor * 0.07)
		print(round(total, 2))
elif cod == "D":
	desc = 0.18
	total = valor - (valor * desc)
	print(round(total, 2))
elif cod == "P":
	desc = 0.18
	total = valor - (valor * desc)
	print(round(total, 2))
