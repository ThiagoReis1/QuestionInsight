valor_de_renda = float(input())
valor_da_prestacao = float(input())

z = valor_de_renda*(35/100)

if valor_da_prestacao > z:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")