valor_renda= float(input("Digite o valor da renda: "))
valor_p= float(input("Digite o valor da prestacao: "))
renda= (valor_renda * (25/100))
if (valor_p > renda):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")