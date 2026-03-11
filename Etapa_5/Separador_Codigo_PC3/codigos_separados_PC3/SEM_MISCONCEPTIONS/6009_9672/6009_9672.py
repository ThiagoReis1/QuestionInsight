renda= float(input("Insira sua renda: "))
prestacao= float(input("Insira o valor da prestacao: "))

if prestacao >= renda * 0.3:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")