a = float(input("valor da renda"))
b = float(input("valor da prestacao"))
c = (a - a * 35/100)


if float(b >= c):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")