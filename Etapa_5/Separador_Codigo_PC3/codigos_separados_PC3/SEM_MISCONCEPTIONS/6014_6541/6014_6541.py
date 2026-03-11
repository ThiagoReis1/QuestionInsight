renda = float(input())
prestacao = float(input())

if prestacao > (renda * 0.35):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")