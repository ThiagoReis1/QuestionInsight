renda = float(input("Informe sua renda: "))
prest = float(input("Informe o valor da parcela mensal: "))

if prest > renda * 0.35:
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")