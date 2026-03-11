r=float(input("Valor de renda: "))
p=float(input("Valor da prestacao: "))


if p > r*(0.35):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	