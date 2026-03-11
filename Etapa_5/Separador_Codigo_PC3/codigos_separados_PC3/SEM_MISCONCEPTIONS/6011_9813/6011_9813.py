renda = float(input())
prestacao = float(input())
limite = renda * 0.35

if prestacao > limite:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")