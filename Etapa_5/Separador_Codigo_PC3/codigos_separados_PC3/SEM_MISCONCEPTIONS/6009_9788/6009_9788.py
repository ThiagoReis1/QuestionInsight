renda = float(input("valor da renda da Dona Fernanda:"))
prestacao = float(input(" prestacao que ela pode pagar por mes:"))
					
limite_prestacao = renda * 0.30

if prestacao > limite_prestacao:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")