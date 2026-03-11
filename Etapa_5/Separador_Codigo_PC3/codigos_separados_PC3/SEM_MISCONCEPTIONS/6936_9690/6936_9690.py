valor = float(input("valor total da compra: "))
codigo = input("D, P ou C?").upper()

if codigo == "D" or codigo == "P":
	total = valor*0.87
elif codigo == "C":
	parc = int(input("1 ou 2?"))
	if parc == 1:
		total=valor
	elif parc==2:
		total = valor*1.08
	else:
		print("numero de parcelas invalido.")
else:
	print("condicao de pagameno invalida.")
	
print(round(total,1))