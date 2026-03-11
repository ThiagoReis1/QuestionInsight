a=float(input("valor da renda:"))
b=float(input("valor da prestacao:"))
renda=a*(35/100)
if b>renda:
	print("Emprestimo nao aprovado")
if b<renda:
	print("Emprestimo aprovado")