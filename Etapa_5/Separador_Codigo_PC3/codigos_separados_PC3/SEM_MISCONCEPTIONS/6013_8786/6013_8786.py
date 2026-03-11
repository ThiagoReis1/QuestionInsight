renda = float(input("Digite aqui a renda: "))
prestacao = float(input("Digite aqui o valor da prestacao: "))

porcentagem = renda * (15 / 100)

if prestacao > porcentagem:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")