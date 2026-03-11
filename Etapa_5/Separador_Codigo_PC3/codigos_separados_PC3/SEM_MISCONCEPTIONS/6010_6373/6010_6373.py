valor_renda = float(input("digite o valor da renda de marcio:"))
valor_prestacao= float(input ("digite o valor da prestacao:"))

if(valor_prestacao> valor_renda*35/100):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")