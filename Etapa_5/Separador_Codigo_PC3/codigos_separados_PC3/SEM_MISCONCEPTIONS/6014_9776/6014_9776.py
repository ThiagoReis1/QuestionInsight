renda=float(input("insira a renda da maria chiquinha: "))
prestacao=float(input("insira o valor da prestacao: "))

parcela=renda *0.35

if prestacao > parcela:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")

