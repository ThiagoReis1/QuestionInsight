renda = float(input("Valor da Renda? "))
prestacao = float(input("Valor Prestacao? "))

aprovacao = renda / 4

if prestacao > aprovacao:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")