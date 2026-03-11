Valor_de_renda = float(input("Qual o valor de renda: "))
Valor_de_prestacao = float(input("Qual o valor da prestacao: "))

porcentagem = Valor_de_renda*(15/100)

if Valor_de_prestacao > porcentagem:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")