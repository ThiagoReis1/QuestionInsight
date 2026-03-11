valor_renda = float(input())
valor_prestacao = float(input())

if valor_prestacao > valor_renda*0.3:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")