renda = float(input("qual eh o valor da renda: "))
prestacao = float(input("qual eh o valor da prestacao: "))

if prestacao > 0.30 * renda:
	print("Emprestimo nao aprovado") 
else:
	print("Emprestimo aprovado")