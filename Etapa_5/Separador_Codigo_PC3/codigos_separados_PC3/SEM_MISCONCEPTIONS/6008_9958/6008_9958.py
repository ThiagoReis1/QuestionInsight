renda = float(input("Valor da renda"))
prestacao = float(input("Valor da prestacao"))

if prestacao > 0.2*renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")