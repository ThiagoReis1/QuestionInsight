renda = float(input("informe o valor da renda: "))
presta = float(input("informe o valor da prestacao: "))

if presta > renda*0.25:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")