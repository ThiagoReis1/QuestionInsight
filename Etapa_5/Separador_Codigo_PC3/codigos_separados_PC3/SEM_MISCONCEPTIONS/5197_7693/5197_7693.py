renda = float(input(" digite o valor da sua renda mensal: "))
prestacao = float(input("digite o valor da prestacao a pagar: "))

valor = renda*0.2

if prestacao > valor:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")