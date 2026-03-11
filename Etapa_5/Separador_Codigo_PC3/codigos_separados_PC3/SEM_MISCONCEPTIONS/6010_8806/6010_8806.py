renda = float(input("Informe o valor da sua renda: "))
prest = float(input("Informe o valor que podes pagar por mes: "))

av = (renda*35)/100

if(prest>av):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")