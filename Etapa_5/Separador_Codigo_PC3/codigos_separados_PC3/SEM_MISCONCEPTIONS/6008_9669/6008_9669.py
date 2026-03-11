valor_renda = float(input("entre com o valor de venda: "))
valor_prest = float(input("entre com o valor de prestacoes: "))

if valor_prest > (20/100 * valor_renda):
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")