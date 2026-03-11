renda = float(input("qual renda: "))
prestacao = float(input("qual prestacao: "))

if (prestacao > renda * 0.25):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")