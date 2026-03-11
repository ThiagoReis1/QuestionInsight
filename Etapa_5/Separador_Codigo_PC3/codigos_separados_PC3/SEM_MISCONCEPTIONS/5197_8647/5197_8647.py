valor_renda = float(input("Qual o valor da renda?: "))
valor_prestacao = float(input("Qual o valor da prestacao?: "))




if (valor_prestacao > valor_renda * 20/100):
	mensagem = "Emprestimo nao aprovado"
	print(mensagem)
	
else:
	(valor_prestacao < valor_renda * 20/100)
	mensagem = "Emprestimo aprovado"
	print(mensagem)