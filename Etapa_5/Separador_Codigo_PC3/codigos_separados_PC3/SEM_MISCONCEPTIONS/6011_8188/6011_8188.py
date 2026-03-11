renda=float(input("qual valor da renda "))
prestacao=float(input("qual o valor da prestacao "))



if prestacao <= 0.35*renda:
	print("Emprestimo aprovado")
	
else:
	print("Emprestimo nao aprovado")
