renda = float(input("renda:"))
vdp = float(input("valor da prestacao:"))

porc = renda * (20/100)

if(vdp > porc):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")