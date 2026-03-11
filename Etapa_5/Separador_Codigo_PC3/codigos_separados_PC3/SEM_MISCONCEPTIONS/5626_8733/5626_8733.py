renda = float(input("escreve a renda da dona clotilde: "))
prest = float(input("valor da prestacao que ela paga: "))

if prest > 0.25* renda:
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")