varR = float(input("Valor da renda: "))
varP = float(input("Valor da prestacao: "))

if varP > varR * 0.2:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")