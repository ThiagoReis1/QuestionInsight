renda = float(input("insira o valor da renda de Dona Clotilde: "))
prestacao = float(input("insira o valor da prestacao que Dona Clotilde tera que pagar por mes: "))

x = 0.25 * renda

if prestacao > x:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")