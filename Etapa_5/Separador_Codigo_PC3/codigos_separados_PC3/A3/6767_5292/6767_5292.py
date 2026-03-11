valor = float(input("digite o valor a ser pago: "))
tipo = input("insira o tipo de pagamento: ").upper()

total = valor

if tipo == "D" or tipo == 'P':
	total = valor * .12
	total = valor - total
	print(round(total, 2))
elif tipo == "C2"  :
	total = valor * .07
	total = valor + total
	print(round(total, 2))
else:
	print(round(total,2))
