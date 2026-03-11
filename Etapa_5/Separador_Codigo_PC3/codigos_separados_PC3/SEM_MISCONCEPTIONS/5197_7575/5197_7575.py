renda=float(input("valor da renda: "))
prestacao=float(input("valor da prestacao: "))
centoR=renda*0.2

if(prestacao<=centoR):
	print("Emprestimo aprovado")
else:
	print("Emprestimo nao aprovado")