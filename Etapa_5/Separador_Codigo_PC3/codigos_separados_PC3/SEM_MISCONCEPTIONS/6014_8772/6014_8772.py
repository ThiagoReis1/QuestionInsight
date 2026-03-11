renda = float(input())
prest = float(input())

porc = 0.35 * renda

if prest > porc:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")