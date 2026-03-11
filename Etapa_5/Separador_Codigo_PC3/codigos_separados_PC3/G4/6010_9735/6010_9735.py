r = float(input("Insira a renda: "))
p = float(input("Insira a prestacao: "))
re = ((35/100)*r)
if p>re:
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")