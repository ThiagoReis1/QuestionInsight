renda = float(input())
prest = float(input())

k = 0.30*renda

if prest > k:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")