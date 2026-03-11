valor_renda = float(input("digite o valor da venda:"))
valor_prestacao = float(input("digite o valor da prestacao:"))

if valor_prestacao > 25/100 * valor_renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")