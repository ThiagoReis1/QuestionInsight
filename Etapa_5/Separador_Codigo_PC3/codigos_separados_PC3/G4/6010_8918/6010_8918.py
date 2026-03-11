r = (input("Digite valor da renda: "))
p = (input("Digite valor da prestação: "))


if (a > 0.35):
	e = r * 0.15
	b = p * 0.15
	a = e + b
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")