renda = float(input("renda"))
prest = float(input("prestacao"))

if prest > renda*(25/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")