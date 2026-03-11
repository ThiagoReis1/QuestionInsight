x = float(input("valor da renda: "))
y = float(input("valor da prestacao: "))
z = x*(35/100)
if y>=z:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")