valorR= float(input("valor da renda: "))
valorP= float(input("valor prestacao: "))

if valorP > valorR * 0.35:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")