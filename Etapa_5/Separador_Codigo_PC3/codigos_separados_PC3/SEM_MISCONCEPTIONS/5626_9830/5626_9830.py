valor_da_renda = float(input("digite o valor da renda: "))
valor_pago = float(input("digite o valor a ser pago: "))
valor_da_prestacao = (valor_da_renda * 25 / 100)

if valor_pago > valor_da_prestacao:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")