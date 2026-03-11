renda=float(input("renda:"))
prestacao=float(input("p:"))

if prestacao>(0.25*renda):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")