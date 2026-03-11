renda= float(input("valor da renda:"))
prest= float(input("prestacao: "))

if prest > renda*(15/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")