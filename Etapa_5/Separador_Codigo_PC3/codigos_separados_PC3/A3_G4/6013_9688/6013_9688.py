x = float(input("Valor da renda:"))
y = float(input("Valor da prestacao:"))
r = 15/100
total= x*(15/100)


if y >= total:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")