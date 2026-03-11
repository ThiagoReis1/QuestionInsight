renda = float(input("Digite a renda de Carlos: "))
prestacao = float(input("Digite o valor da prestacao: "))

renda1 = renda * 20/100
if prestacao > renda1:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")