x = float(input("valor da renda: "))
y = float(input("valor da prestacao: "))

if y>(25/100) * x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")