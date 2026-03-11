valordar = float(input("valor da renda: "))
valordap = float(input("valor da prestacao: "))
X = valordap/valordar
if (X > 0.25):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")