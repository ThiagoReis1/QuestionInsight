r = float(input("valor da renda: "))
p = float(input("valor da pretacao: "))
if p > r*(25/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")