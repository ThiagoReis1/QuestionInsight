ren = float(input("valor da renda: "))
prest = float(input("valor de prestacao: "))
if prest>ren*(15/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")