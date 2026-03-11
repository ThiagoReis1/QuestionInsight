renda = float(input("valor:"))
prest = float(input("prestacao:"))
porcentagem = renda * (35/100)

if prest > porcentagem:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")