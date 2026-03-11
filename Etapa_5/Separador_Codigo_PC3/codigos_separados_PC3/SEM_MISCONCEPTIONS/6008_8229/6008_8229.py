renda = float(input("Digite o valor da renda mensal de seu Marcio:"))
prestacao = float(input("Digite o valor da prestacao mensal do emprestimo: "))
limite = renda * (20/100)
if prestacao <= limite:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")