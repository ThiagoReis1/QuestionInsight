renda = float(input("digite o valor da renda da maria chiquinha: "))
prestacao = float(input("digite o valor que ela pode pagar por mes: "))

limite_porcentagem = 0.35

if prestacao > renda * limite_porcentagem:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")