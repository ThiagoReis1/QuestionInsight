renda = float(input("Valor da renda de Dona Carla: "))
prestacao = float(input("Valor da prestacao: "))

porcentagem = renda * (35/100)

if prestacao > porcentagem:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")