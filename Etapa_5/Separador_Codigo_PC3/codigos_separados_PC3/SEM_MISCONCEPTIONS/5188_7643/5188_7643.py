renda = float(input("Valor da renda: "))
prestacao = float(input("Valor da pretacao: "))

a = renda + 0.25 * prestacao
if a > renda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")