renda = float(input("Valor da renda: "))
vp = float(input("Valor da prestacao: "))
em = (renda*25/100)

if vp>em: 
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")