renda = float(input("Valor da renda da Dona Clotilde: "))
prestacao = float(input("Valor da prestacao que ela pode pagar por mes: "))
porc = renda*(25/100)
if prestacao > porc :
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	