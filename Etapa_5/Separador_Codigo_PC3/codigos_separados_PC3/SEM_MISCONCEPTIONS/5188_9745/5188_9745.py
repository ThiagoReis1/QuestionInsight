renda = float(input("valor da renda:"))
prest = float(input("valor da prestacao:"))

if prest <= (1/4)*renda:
	print("Emprestimo aprovado")
	
else:
	print("Emprestimo nao aprovado")