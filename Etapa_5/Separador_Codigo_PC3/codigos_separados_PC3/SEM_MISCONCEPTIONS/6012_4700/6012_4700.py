renda = float(input("Valor da renda: "))
prestacao = float(input("Valor da prestacao: "))

if (prestacao > ((25/100)*renda)):
	print ("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")