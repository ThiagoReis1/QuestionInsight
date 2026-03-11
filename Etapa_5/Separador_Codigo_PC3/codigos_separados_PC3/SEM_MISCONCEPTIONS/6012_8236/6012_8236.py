valor_da_renda = float(input("digite o valor da renda: "))
valor_da_prestacao = float(input("digite o valor da prestacao: "))
x = valor_da_renda * 0.25
if valor_da_prestacao > x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")