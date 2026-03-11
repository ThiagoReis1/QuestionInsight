valor = float(input("insira o valor total da compra: "))
codigo = input("insira o codigo da opcao de pagamento (D/P/C): ").upper()

if codigo == "C":
	vezes = int(input("em quantas vezes? "))
	if vezes == 1:
		total = valor
		print(round(total, 2))
		
	elif vezes == 2:
		total = valor + (valor * 0.08)
		print(round(total, 2))
		
elif codigo == "P" or codigo == "D":
	total = valor - (valor * 0.13)
	print(round(total, 2))