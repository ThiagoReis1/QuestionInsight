v = float(input("valor da renda:"))
p = float(input("valor da prestacao:"))
if p > v*(25/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")