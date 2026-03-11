renda = float(input("digite o valor da renda: "))
prestacao = float(input("digite o valor da prestacao: "))
if prestacao > 0.35* renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")