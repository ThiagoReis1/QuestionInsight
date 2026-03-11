renda = float(input())
prest = float(input())

porcent = renda*(20/100)
if prest > porcent:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")