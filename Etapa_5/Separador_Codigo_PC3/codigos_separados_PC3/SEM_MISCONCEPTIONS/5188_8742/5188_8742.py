renda = float(input("Qual a renda de Florinda: "))
prestacao = float(input("Quanto e a prestacao: "))
if prestacao > renda * 0.25:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")