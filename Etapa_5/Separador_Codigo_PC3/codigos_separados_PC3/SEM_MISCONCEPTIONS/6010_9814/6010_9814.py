renda = float(input("renda de marcio: "))
prest = float(input("valor da prestacao: "))

porc = renda * 35/100

if prest > porc:
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")