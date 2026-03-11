maria= float(input("valor da venda: "))
imprest= float(input("valor da prestacao: "))
per = (35/100)*maria
if (per<imprest):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")
