renda = int(input("Digite o valor da renda de Dona Clotilde: "))
prestacao = int(input("Digite o valor da prestacao que ela pretende pagar por mes: "))
valor = 0.25 * renda
if prestacao > valor:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")