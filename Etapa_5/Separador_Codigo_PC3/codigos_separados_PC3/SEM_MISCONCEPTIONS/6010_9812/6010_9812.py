renda = float(input("Valor renda: "))
prest = float(input("Valor prestacao: "))

a = renda * .35

if prest > a:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")