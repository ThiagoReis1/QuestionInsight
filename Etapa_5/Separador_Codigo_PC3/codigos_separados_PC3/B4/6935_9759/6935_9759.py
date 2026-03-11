valr = float(input("Informe o valor total da compra: "))
cod = input("Informe o a forma de pagamento: ").upper()

if cod == "D":
	total = valr - (valr * (12/100))
	print(round(total, 2))
elif cod == "C":
	vezes = int(input("Informe de quantas vezes sera o pagamento: "))
	if vezes == 1:
		print(round(valr, 2))
	else:
		total = valr + (valr * (7/100))
		print(round(total, 2))
else:
	total =  valr - (valr * (12/100))
	print(round(total, 2))