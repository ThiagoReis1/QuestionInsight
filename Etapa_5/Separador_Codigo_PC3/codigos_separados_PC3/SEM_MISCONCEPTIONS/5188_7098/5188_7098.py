renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

p_renda = renda * 25/100
if prestacao > p_renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	