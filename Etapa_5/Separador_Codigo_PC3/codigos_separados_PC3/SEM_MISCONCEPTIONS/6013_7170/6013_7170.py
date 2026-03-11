renda = float(input("Qual a renda?: "))
prestacao = float(input("Valor da prestacao?: "))

if prestacao > (renda*0.15):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")