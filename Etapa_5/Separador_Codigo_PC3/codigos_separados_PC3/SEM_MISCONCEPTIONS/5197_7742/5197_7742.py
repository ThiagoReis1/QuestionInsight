renda = float(input("Digite o valor da renda: "))
prestacao = float(input("Digite o valor que pode pagar por mes: "))
				  
if (prestacao > renda * 0.2):
	print ("Emprestimo nao aprovado")
else:
	print ("Emprestimo aprovado")