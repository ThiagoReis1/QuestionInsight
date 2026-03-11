renda = float(input("valor da renda: "))
prt = float(input("valor da prestacao: "))

r = renda * (35/100)

if(prt > r):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")