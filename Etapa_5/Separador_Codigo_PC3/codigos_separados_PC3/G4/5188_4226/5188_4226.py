r = float(input("renda "))
p = float(input("prestacao "))

if p > 0.25*r:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")