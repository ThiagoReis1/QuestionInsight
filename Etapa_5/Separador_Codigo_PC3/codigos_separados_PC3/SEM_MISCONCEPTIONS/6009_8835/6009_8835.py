renda = float(input("valor:"))
pr = float(input("prestacao:"))
x = (100 * pr)/ renda
if (x) >= 30:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")