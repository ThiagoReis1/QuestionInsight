renda_Carla = float(input("Qual o valor da sua renda, dona Carla? "))
prestacao_mensal_Carla = float(input("Quanto voce pode pagar por mes, Dona Carla? "))

if (prestacao_mensal_Carla > (renda_Carla * (35/100))):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")	