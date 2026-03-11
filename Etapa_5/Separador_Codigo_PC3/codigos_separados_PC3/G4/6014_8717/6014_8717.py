vr = float(input("Valor da renda de Maria Chiquinha: "))
vp = float(input("Valor da prestacao: "))

if (vp > (vr*(35/100))):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")