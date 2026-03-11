renda = float(input("valor da renda"))
prest = float(input("valor da prestacao"))

if prest > .15*renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")