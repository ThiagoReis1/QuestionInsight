renda = float(input("valor da renda:"))
prest = float(input("valor da prestacao:"))



if prest >= renda * .25 :
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")