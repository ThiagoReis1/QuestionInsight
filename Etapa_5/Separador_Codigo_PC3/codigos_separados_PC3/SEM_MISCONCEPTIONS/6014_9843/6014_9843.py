renda = float(input("Digite o valor da renda de Maria Chiquinha:"))
prestacao = float(input("Digite o valor da prestacao que pode ser paga ao mes pela Maria: "))

margem = renda * (35/100)

if (prestacao > margem):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")