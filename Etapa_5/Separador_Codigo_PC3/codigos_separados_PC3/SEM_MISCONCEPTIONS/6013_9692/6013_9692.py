renda = float(input("insira o valor da renda: "))
p = float(input("insira o valor da prestacao: "))
x = (0.15*renda)
if p >= x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
