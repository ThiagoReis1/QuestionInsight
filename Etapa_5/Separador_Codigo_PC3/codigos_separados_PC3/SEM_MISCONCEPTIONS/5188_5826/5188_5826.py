renda = float(input("Digite o valor da renda de Dona Florinda: "))
prestacao = float(input("Digite o valor da prestacao: "))

if(prestacao > 0.25*renda):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")