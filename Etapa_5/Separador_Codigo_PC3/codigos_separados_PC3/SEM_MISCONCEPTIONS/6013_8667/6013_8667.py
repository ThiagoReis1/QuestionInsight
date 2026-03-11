renda = float(input("Digite o avlor da renda: "))
prest = float(input("Digite o avlor da prestacao: "))

por = 15/100*renda

if(prest > por):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")