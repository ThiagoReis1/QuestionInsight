valor_compra = float(input("Digite o valor da compra:"))
codigo = input("Digite o codigo da opcao de pagamento:")

if codigo == 'D':
	valor_pago = valor_compra - (valor_compra*0.13)
	print(round(valor_pago,2))
elif codigo == 'P':
	valor_pago = valor_compra - (valor_compra*0.13)
	print(round(valor_pago,2))
elif codigo == 'C':
	vezes = int(input("PAgar de 1 ou 2 vezes"))
	if vezes == 1:
		print(round(valor_compra,2))
	else:
		valor_pago = valor_compra+(valor_compra*0.08)
		print(round(valor_pago,2))