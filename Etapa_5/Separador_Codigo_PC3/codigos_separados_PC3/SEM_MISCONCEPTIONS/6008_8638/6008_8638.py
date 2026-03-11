renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))

x= renda * (20/100)

if (prestacao > x):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")