valrenda = float(input("Valor da renda: "))
valprestacao = float(input("Valor da prestacao: "))

percrenda = valrenda * 0.35
if valprestacao > percrenda:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")