renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

if prestacao > 25/100 * renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")